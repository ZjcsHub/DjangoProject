from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo,HeroInfo
# Create your views here.

# 定义视图函数 HttpRequest
# 进行url配置，建立URl地址和视图对应关系

def index(request):
    # 进行处理 和 M 和 T 交互
    # 加载模板文件
    # 1.加载模板文件
    temp = loader.get_template('booktest/index.html')
    # 2.定义模板上下文，给模板文件传递数据
    context = {}#RequestContext(request,{})
    # 3.模板渲染，产生标准的html内容
    res_html = temp.render(context)
    # 4.返回给浏览器
    return HttpResponse(res_html)


def index2(request):
    return render(request,'booktest/index.html',{'context':'hello world','lists':list(range(1,10))})




def show_books(request):
    # 查找图书信息
    books = BookInfo.objects.all()
    return render(request,'booktest/show_books.html',{"books":books})



def detail(request,bid):
    # 查询图书关联的英雄信息
    # 根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 查询和book关联的信息
    heros = book.heroinfo_set.all()
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})
