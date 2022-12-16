from django.shortcuts import render,redirect,reverse
import re
from .models import User
from django.views.generic import View
# Create your views here.
from itsdangerous import URLSafeTimedSerializer,SignatureExpired # 加密
from django.conf import settings
from django.http import HttpResponse
from celery_tasks.tasks import send_register_active_email


class RegisterView(View):
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
    def get(self,request):
        return render(request,'login.html')