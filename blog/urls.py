from django.urls import path

from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('post/<str:pk>', PostView.as_view(), name='post'),
]
