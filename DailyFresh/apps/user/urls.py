from django.urls import path
from .views import RegisterView,ActiveView,LoginView
urlpatterns = [
    path('register',RegisterView.as_view(),name='register'), # 注册
    path('active/<token>',ActiveView.as_view(),name='active'),# 激活
    path('login',LoginView.as_view(),name='login') # 登录
]



