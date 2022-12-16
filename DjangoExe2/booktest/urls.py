from django.urls import path
from booktest import views
urlpatterns = [
    path('',views.index),
    path('create',views.create),
    path('delete/<bid>',views.delete),
    path('area',views.areas),
    path('temp_tags',views.temp_tags),
    path('temp_filter',views.temp_filter),
    path('extention',views.exten_templete),
    path('html_escape',views.html_escape), # html 转义
    path('show_areas/<p_index>',views.show_areas,name='showareas'),
    path('select_areas',views.select_areas),
    path('prov',views.prov),
    path('city',views.city)

]