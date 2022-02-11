from .views import *
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    #path("", cache_page(60*30)(ProjectsListView.as_view()), name="projects"),
    path("", ProjectsListView.as_view(), name="projects"),
    path("project/<str:pk>", ProjectView.as_view(), name="project"),
]
