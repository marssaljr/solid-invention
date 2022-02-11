from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    #path("", cache_page(0)(BlogListView.as_view()), name="blog_list"),
    path("", BlogListView.as_view(), name="blog_list"),
    path("post/<str:pk>", PostView.as_view(), name="post"),
]
