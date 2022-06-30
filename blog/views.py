from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def posts(request):
    posts = Post.objects.filter(published=True). order_by('-created_at')
    return  render(request, 'index.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
