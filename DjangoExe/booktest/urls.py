from django.urls import path
from booktest import views

urlpatterns = [

    path('index',views.index),
    path('index2',views.index2),
    path('books',views.show_books),
    path('books/<bid>',views.detail)

]