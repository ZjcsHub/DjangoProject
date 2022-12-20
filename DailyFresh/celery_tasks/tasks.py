# celery 使用
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail # 发送邮件

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DailyFresh.settings')
django.setup()
from django.template import loader
from apps.goods.models import GoodsType,IndexGoodsBanner,IndexPromotionBanner,IndexTypeGoodsBanner
# 创建Celery对象
# 中间人使用 redis
app = Celery('celery_taske.tasks',broker='redis://127.0.0.1:6379/1')


# 定义任务函数
@app.task
def send_register_active_email(request_url,to_email,username):
    '''发送激活邮件'''
    subject = 'JcKeats项目欢迎信息'
    message = "欢迎使用JcKeats注册系统"
    from_email = settings.EMAIL_FROM
    recipient_list = [to_email] # 收件人列表
    html_message = '<h1>%s 欢迎您使用JcKeats项目，请点击请求激活您的账户:<a href="%s">立即激活</a></h1>' %(username,request_url)
    send_mail(subject,message,from_email,recipient_list,html_message=html_message)

# 启动worker
# celery -A celery_tasks.tasks worker -l info

# 产生首页静态页面
@app.task
def generate_static_index_html():
    '''产生首页静态页面'''
    # 获取商品的种类信息
    types = GoodsType.objects.all()

    # 获取首页轮播商品信息
    goods_banners = IndexGoodsBanner.objects.all().order_by('index')

    # 获取首页促销活动信息
    promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

    # 获取首页分类商品展示信息
    for type in types: # GoodsType
        # 获取type种类首页分类商品的图片展示信息
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
        # 获取type种类首页分类商品的文字展示信息
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')

        # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
        type.image_banners = image_banners
        type.title_banners = title_banners

    context = {'types': types,
               'goods_banners': goods_banners,
               'promotion_banners': promotion_banners}

    # 加载模板文件
    temp = loader.get_template('static_index.html')
    static_index_html = temp.render(context)

    # 生成静态页面
    savePath = settings.BASE_DIR / 'static/index.html'
    print(savePath)
    with open(savePath,'w') as w:
        w.write(static_index_html)