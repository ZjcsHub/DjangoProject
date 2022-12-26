from django.urls import path
from .views import HomePage,DetailView,ListView
urlpatterns = [
    path("",HomePage.as_view(),name='index'),
    path('goods/<goods_id>',DetailView.as_view(),name='detail'),
    path('list/<type_id>/<page>',ListView.as_view(),name='list') # 列表页
]



