from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-dodano')
    template_name = 'inne/post.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'inne/post_detail.html'
