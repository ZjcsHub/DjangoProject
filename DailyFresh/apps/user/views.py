from django.shortcuts import render,redirect,reverse
import re
from .models import User,Address
from django.views.generic import View
# Create your views here.
from itsdangerous import URLSafeTimedSerializer,SignatureExpired # 加密
from django.conf import settings
from django.http import HttpResponse
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate,login,logout
from util.LoginMixin import LoginRequiredMixin
from django_redis import get_redis_connection
from apps.goods.models import GoodsSKU
class RegisterView(View):
    '''用户注册'''
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        # 接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        rePassword = request.POST.get('cpwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # 进行数据校验
        if not all([username,password,rePassword,email]):
            # 数据不完整
            return render(request,'register.html',{'errmsg':'数据不完整'})

        # 校验邮箱
        if not re.match(r'^[a-zA-Z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
            return render(request,'register.html',{'errmsg':'邮箱不完整'})

        if allow != 'on':
            return render(request,'register.html',{'errmsg':'请同意协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名已存在
            user = None
        if user:
            # 用户名已存在
            return render(request,'register.html',{'errmsg':'用户名已存在'})
        # 进行业务处理：用户注册
        user = User.objects.create_user(username,email,password)
        user.is_active = 0
        user.save()

        # 发送激活邮件，包含激活链接
        # 激活链接中需要包含加密信息 pip install itsdangerous
        # 加密用户身份信息，生成激活token
        serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
        info = {'confirm':user.id}
        token = serializer.dumps(info)
        # 发邮件
        scheme = request.scheme
        host = request.META['HTTP_HOST']
        path = redirect('user:active',token).url
        request_url = scheme + "://" + host + path
        print(request_url)
        send_register_active_email.delay(request_url,email,username,token)
        # 返回应答,跳转首页
        return redirect(reverse('goods:index'))

class ActiveView(View):
    '''激活用户'''
    def get(self,request,token):
        '''激活用户'''
        # 获取激活用户信息
        serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
        try:
            info = serializer.loads(token,max_age=3600)
            user_id = info['confirm']
            # 根据ID获取信息
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            # 跳转登录
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            print("激活链接已过期",e)
            return HttpResponse('激活链接已过期')


class LoginView(View):
    '''登录页面'''
    def get(self,request):
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('username')
            check = "checked"
        else:
            username = ""
            check = ""
        return render(request,'login.html',{'username':username,'check':check})

    def post(self,request):

        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 校验数据
        if not all([username,password]):
            return render(request,'login.html',{'errmsg':'数据不完整'})

        user = authenticate(request,username=username,password=password)

        if user:
            # 登录成功
            if user.is_active:
                # 记录登录状态，使用系统登录
                login(request,user)

                response = redirect(reverse('goods:index'))

                # 判断是否需要记住用户名
                remember = request.POST.get('remember')
                if remember == 'on':
                    response.set_cookie('username',username,max_age=7*24*3600)
                else:
                    response.delete_cookie('username')
                return response
            else:
                # 未激活
                return render(request,'login.html',{'errmsg':'用户未激活'})
        else:
            # 登录失败
            return render(request,'login.html',{'errmsg':'用户名或密码错误'})

class LogOutView(View):
    '''退出登录'''
    def get(self,request):
        user = request.user
        print("----",user)
        if user:
            logout(request)

        return redirect(reverse('goods:index'))

class UserInfoView(LoginRequiredMixin,View):
    '''用户信息页'''
    def get(self,request):
        # 获取用户个人信息
        user = request.user
        address = Address.objects.get_default_address(user)
        # 获取用户历史浏览记录
        con = get_redis_connection()
        history_key = 'history_%d' %user.id
        sku_ids = con.lrange(history_key,0,4)
        # 从数据库中查商品
        # goods_li = GoodsSKU.objects.filter(id__in=sku_ids)
        goods_li = []
        for skuid in sku_ids:
            goods = GoodsSKU.objects.get(id=skuid)
            goods_li.append(goods)

        contents = {'page':'user','address':address,'goods':goods_li}

        return render(request,'user_center_info.html',contents)



class UserOrderView(LoginRequiredMixin,View):
    '''用户订单页'''
    def get(self,request):
        # 获取用户订单信息
        return render(request,'user_center_order.html',{'page':'order'})


class AddressView(LoginRequiredMixin,View):
    '''用户地址页'''
    def get(self,request):
        # 获取用户默认地址
        try:
            address = Address.objects.get_default_address(request.user)
        except Address.DoesNotExist:
            address = None

        return render(request,'user_center_site.html',{'page':'address','address':address})

    def post(self,request):
        # 接收数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        # 校验数据
        if not all([receiver,addr,phone]):
            return render(request,'user_center_site.html',{'errmsg':'数据不完整'})
        # 校验手机号
        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$',phone):
            return render(request,'user_center_site.html',{'errmsg':'手机号码不正确'})
        # 业务处理
        try:
            address = Address.objects.get_default_address(request.user)
        except Address.DoesNotExist:
            address = None


        if address:
            is_default = False
        else:
            is_default = True
        # 添加地址
        Address.objects.create(user=request.user,receiver=receiver,addr=addr,zip_code=zip_code,phone=phone,is_default=is_default)
        # 返回应答
        return redirect(reverse('user:address'))