# celery 使用
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail # 发送邮件
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DailyFresh.settings')

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