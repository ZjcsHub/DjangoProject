from django.shortcuts import render,redirect
from .models import BookInfo,HeroInfo,AreaInfo
from datetime import date
from django.core.paginator import Paginator # 分页
from django.http import JsonResponse
# Create your views here.

def index(request):
    # 查询所有图书信息
    books = BookInfo.objects.all()
    # 使用模板
    return render(request,'booktest/index.html',{'books':books})

def create(request):
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpubdate = date(1999,1,1)
    book.save()

    return redirect(index)

def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    if book != None:
        book.isDelete = True
        book.save()
    return redirect(index)


def areas(request):
    '''获取广州市的上级地区及下级地区'''
    # 获取广州市的信息
    area = AreaInfo.objects.get(atitle='广州市')
    # 查询广州市的上级地区
    parent = area.aParent
    # 查询广州市的下级地区
    children = area.areainfo_set.all()

    return render(request,'booktest/area.html',{'area':area,'parent':parent,'children':children})


def temp_tags(request):

    books = BookInfo.objects.all()

    return render(request,'booktest/temp_tags.html',{'books':books})

def temp_filter(request):
    books = BookInfo.objects.all()

    return render(request,'booktest/temp_fliter.html',{'books':books})

def exten_templete(request):
    return render(request,'booktest/child.html')


def html_escape(request):
    '''html 转义'''
    return render(request,'booktest/html_escape.html',{'contents':'<h2>html 转义</h2>'})

# 前段访问传页码
def show_areas(request,p_index):
    '''显示所有省份信息'''
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 分页
    paginator = Paginator(areas,20)
    print(paginator.num_pages) # 页码数
    print(paginator.page_range) # 页码列表
    # 获取第一页内容
    if p_index == None:
        pindex = 1
    else:
        pindex = int(p_index)
    page = paginator.page(pindex)
    print(page.number) # 当前页码
    return render(request,'booktest/show_areas.html',{'page':page})


def select_areas(request):
    '''显示城市地区'''
    return render(request,'booktest/select_area.html')

def prov(request):
    '''获取所有省级地区信息'''
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 遍历ares 拼接json 标题 id
    area_list = []
    for area in areas:
        area_list.append({'id':area.id,'title':area.atitle})

    return JsonResponse({'data':area_list})

def city(request):

    prov_id = request.GET.get('id')
    print(prov_id)
    areas = AreaInfo.objects.filter(aParent__id=prov_id)
    area_list = []
    for area in areas:
        area_list.append({'id':area.id,'title':area.atitle})

    return JsonResponse({'data':area_list})