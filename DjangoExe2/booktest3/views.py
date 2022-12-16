from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Pictest
# Create your views here.

def static_test(request):
    '''静态文件测试'''


    return render(request,'booktest3/static_test.html')


def index(request):
    '''获取浏览器端ip地址'''
    ip = request.META['REMOTE_ADDR']
    print(ip)
    return render(request,'booktest3/index.html',{"ip":ip})

# 上传图片
def show_pic(request):
    return render(request,'booktest3/picture_upload.html')

def upload_pic(request):
    # 1.获取上传图片
    # 上传文件处理对象
    file = request.FILES.get('pic')
    # <MultiValueDict: {'pic': [<TemporaryUploadedFile: 00_first setup.jpg (image/jpeg)>]}>

    print(file)

    picModel = Pictest()
    picModel.goods_pic = file
    picModel.save()


    # # 2.创建文件
    # name = file.get('pic')
    # # save_path = '%s/booktest3/%s' %(settings.MEDIA_ROOT,name)
    # # with open(save_path,'wb') as f:
    #
    # # 3.获取上传文件内容，并写入创建文件中
    # # 4.保存上传路径
    return HttpResponse('OK')

def show_all_pic(request):

    picLists = Pictest.objects.all()

    return render(request,'booktest3/showUploadpic.html',{'picList':picLists})