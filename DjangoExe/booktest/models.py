from django.db import models

# Create your models here.
# 设计表模型类


# 1. 生成迁移文件
# python manage makemigrations
# 2. 执行迁移生成表
# python manage migrate


# 图书类
class BookInfo(models.Model):
    '''图书模型类'''
    # CharField 说明是一个字符串，max_length 指定字符串最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期，DateField 说明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名
        return self.btitle

# 英雄人物类
class HeroInfo(models.Model):
    '''英雄人物模型'''
    hname = models.CharField(max_length=20)
    # 性别， BooleanField 说明是Bool类型，false表示男
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性 对应表的字段名 为 关系属性名_id
    hbook = models.ForeignKey('BookInfo',null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.hname