from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(ListView):
    model = Post
    template_name = 'post_detail.html'


# Create your views here.
