from django.urls import path
from . import views
urlpatterns = [
    path('register',views.RegisterView.as_view(),name='register'), # 注册
    path('active/<token>',views.ActiveView.as_view(),name='active'),# 激活
    path('login',views.LoginView.as_view(),name='login'),# 登录
    path('user',views.UserInfoView.as_view(),name='user'),# 用户中心
    path('order',views.UserOrderView.as_view(),name='order'),# 订单
    path('address',views.AddressView.as_view(),name='address'),# 地址
    path('logout',views.LogOutView.as_view(),name='logout') # 登出
]



