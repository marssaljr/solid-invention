from django.views.generic import ListView, DetailView
from .models import Project


class ProjectsListView(ListView):
    model = Project
    template_name = "projects.html"


class ProjectView(DetailView):
    model = Project
    template_name = "project.html"
