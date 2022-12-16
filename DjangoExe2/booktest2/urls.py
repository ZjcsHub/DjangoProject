from django.urls import path
from booktest2 import views
urlpatterns = [
    path('showarg<id>',views.showArg,name='showarg'),
    path('login',views.login),
    path('login_check',views.loginCheck),
    path('testajax',views.test_ajax),
    path('ajax_handle',views.ajax_handle),
    path('login_ajax',views.login_ajax),
    path('login_ajax_check',views.login_ajax_check),
    path('setcookie',views.set_cookie),
    path('getcookie',views.get_cookie),
    path('setsession',views.set_session),
    path('getsession',views.get_session),
    path('clearsession',views.clear_session),
    path('changepwd',views.change_pwd),
    path('view_code',views.view_code),
    path('url_reverse',views.url_reverse),
    path('test_redirect',views.test_redirect)
]