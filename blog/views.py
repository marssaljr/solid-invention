from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostView(DetailView):
    model = Post
    template_name = "post.html"
