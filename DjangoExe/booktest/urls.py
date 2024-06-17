from django.urls import path
from booktest import views
from revproxy.views import ProxyView
from django.urls import re_path

urlpatterns = [

    path('index',views.index),
    path('index2',views.index2),
    path('books',views.show_books),
    path('books/<bid>',views.detail),
    path('redirect',views.redirectDemo),
    # path('redirect2/<path>',ProxyView.as_view(upstream='http://www.zdfit.net/maps_en.html')),
    re_path(r'redirect2/(?P<path>.*)', ProxyView.as_view(upstream='http://www.zdfit.net/')),
]