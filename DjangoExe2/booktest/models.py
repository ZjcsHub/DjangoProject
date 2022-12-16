from django.db import models

class BookInfoManager(models.Manager):
    '''图书模型管理类'''
    # 改变查询结果集
    def all(self):
        # 获取所有数据
        # 调用父类all方法
        books = super().all()
        # 对数据过滤
        return books.filter(isDelete=False)

    # 2.封装函数，操作模型类对应的数据表
    def create_book(self,btitle,bpub_date):
        # 创建图书对象
        # obj = BookInfo()
        model_class = self.model
        obj = model_class()
        obj.btitle = btitle
        obj.bpubdate = bpub_date
        obj.save()
        return obj

# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    # 图书名称
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpubdate = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    # 自定义一个管理对象
    objects = BookInfoManager()

    # 指定表名
    # 元选项
    # class Meta:
    #     db_table = 'bookinfo'

    def __str__(self):
        return self.btitle

class HeroInfo(models.Model):
    '''英雄模型类'''
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)
    # 关系属性
    hbook = models.ForeignKey('BookInfo',null=True,on_delete=models.SET_NULL)
    # 逻辑删除
    isDelete = models.BooleanField(default=False)

    # class Meta:
    #     db_table = 'heroinfo'

    def __str__(self):
        return self.hname
'''

class NewsType(models.Model):
    type_name = models.CharField(max_length=20)

class NewsInfo(models.Model):
    title = models.CharField(max_length=128)
    #内容
    content = models.TextField()
    # 创建时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 关系属性
    news_type = models.ManyToManyField('NewsType')
'''

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20,verbose_name='标题')
    # 关系属性。代表当前地区的父级地区
    aParent = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL,verbose_name='父级地区')

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle
    # 添加排序
    title.admin_order_field = 'atitle'
    title.short_description = '标题' # 显示中文名称
    # class Meta:
    #     db_table = 'areainfo'

    def parent(self):
        return self.aParent.atitle if self.aParent else ""
    parent.admin_order_field = 'atitle'
    parent.short_description = '父级标题'
