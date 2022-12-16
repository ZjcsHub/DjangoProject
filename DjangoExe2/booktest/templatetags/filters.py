# 自定义过滤器
from django.template import Library
from django.conf import settings
# 创建一个Library对象
register = Library()

@register.filter
def mod(num):
    '''判断num是否是偶数'''
    return num % 2

@register.filter
def mod_val(num,val):
    '''判断num能否被val整除'''
    return num % val

@register.filter
def header_image(headerimage):
    if headerimage.name == "":
        return settings.STATIC_URL + "media/default_header.png"

    return settings.STATIC_URL + "media/" + headerimage.url

