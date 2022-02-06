from django.urls import path
from django.views.generic import TemplateView

# from .views import HomeView

urlpatterns = [
#    path('', HomeView.as_view(), name='home'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
