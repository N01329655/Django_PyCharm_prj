from django.shortcuts import render

# my imports
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_details_object'
