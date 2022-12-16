from django.urls import path
from booktest3 import views
urlpatterns = [
    path('static_test',views.static_test,name='staticTest'),
    path('index',views.index,name='index'),
    path('show_pic',views.show_pic,name='showpic'),
    path('upload_pic',views.upload_pic,name='uploadpic'),
    path('show_all_pic',views.show_all_pic),
]