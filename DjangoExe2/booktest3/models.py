from django.db import models
from tinymce.models import HTMLField
# Create your models here.

# 上传图片
class Pictest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to='booktest3') # 上传目录
    class Meta:
        verbose_name = "图片测试"
        verbose_name_plural = "图片测试"

class GoodsTest(models.Model):
    '''测试多文本类型'''
    STATUS_CHOICES = (
        (0,'下架'),
        (1,'上架')
    )

    status = models.SmallIntegerField(choices=STATUS_CHOICES,verbose_name='商品状态')
    # 富文本
    detail = HTMLField(verbose_name="商品详情")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"