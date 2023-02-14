
from django.urls import path
from .views import IndexView,TopicView,TopicDetailView,ChatGPTView
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('topic',TopicView.as_view(),name='topic'),
    path('topics/<topic_id>',TopicDetailView.as_view(),name='topic_detail'),
    path('chatgpt',ChatGPTView.as_view(),name='chatgpt')
]
