from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.

# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ["id","btitle","bpub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id","hname","hgender","hcomment","hbook"]

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
