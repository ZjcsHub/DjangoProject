from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime,timedelta
from .verify_code import verify_code
# Create your views here.

def showArg(request,id):
    return render(request, 'booktest2/index.html', {'num':id})


def login(request):
    '''显示登录页面'''
    # 获取cookie用户名
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''

    return render(request,'booktest2/login.html',{'username':username})

def loginCheck(request):
    # 获取提交的用户名和密码
    # request.POST 保存的是post提交参数
    # .QueryDict
    # request.GET 保存get提交参数
    print(request.method)
    print(request.path)
    print(type(request.POST))
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # 验证码
    viewcode = request.POST.get("viewcode")
    viewcode2 = request.session.get("verifycode")
    # 进行验证码校验
    if viewcode != viewcode2:
        # 验证码错误
        return redirect(login)


    print(username,password)
    # 进行登录校验
    # 实际开发根据用户名和密码查找数据库
    if username == 'smart' and password == '123':
        # 用户名密码正确。跳转首页

        response = redirect(showArg,2)

        if remember == 'on':
            response.set_cookie('username',username,max_age=7*24*3600)

        return response
    else:
        # 用户名密码错误
        return redirect(login)

    # 返回应答

def test_ajax(request):
    return render(request,'booktest2/test_ajax.html')

def ajax_handle(request):
    '''检查ajax'''
    return JsonResponse({"code":200})


def login_ajax(request):
    return render(request,'booktest2/login_ajax.html')

def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    return JsonResponse({'code':1})

# cookie 和 seccion
# 设置cookie 需要一个HttpResponse类的对象，或者它子类对象
def set_cookie(request):
    '''设置cookie信息'''
    reponse = HttpResponse('设置cookie')
    reponse.set_cookie('num',1)
    # 设置cookie 过期时间
    reponse.set_cookie('second',12,max_age=14*24*3600)
    reponse.set_cookie('minute',12,expires=datetime.now() + timedelta(days=14))
    return reponse

def get_cookie(request):
    cookie = request.COOKIES
    num = cookie.get('num')
    return HttpResponse(num)

def set_session(request):
    request.session["username"] = "smart"
    request.session["age"] = 18
    request.session.set_expiry(10) # 10s后过期
    return HttpResponse("设置session")

def get_session(request):
    username = request.session["username"]
    age = request.session["age"]
    return HttpResponse(username + ":" + str(age))

def clear_session(request):
    request.session.clear() # 清除session数据
    request.session.flush() # 清除session整条数据
    del request.session["key"] # 删除某一个key
    return HttpResponse("清除OK")

# 装饰器函数
def login_required(view_func):
    def weapper(request,*args,**kwargs):
        # 判断用户是否登录
        if request.session.has_key('islogin'):
            return view_func(request,*args,**kwargs)
        else:
            return redirect(login)
    return weapper

@login_required
def change_pwd(request):
    # 进行用户判断
    # if not request.session.has_key("islogin"):
    #     return redirect(login)
    return HttpResponse("change pawword")


# 验证码
def view_code(request):
    verifycode,data,type = verify_code()
    request.session["verifycode"] = verifycode
    return HttpResponse(data,type)


def url_reverse(request):
    '''url 反向解析'''
    return render(request,'booktest2/url_request.html')

from django.shortcuts import reverse
def test_redirect(request):
    '''url 反向解析'''
    # url = reverse('booktest2:showarg',args="2")
    url = reverse('booktest2:showarg',kwargs={"id":2})
    print(url)
    return redirect(url)