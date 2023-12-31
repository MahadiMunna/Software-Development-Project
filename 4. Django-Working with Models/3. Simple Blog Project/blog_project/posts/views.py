from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('home')
    else:
        post = PostForm()
    return render(request, 'add_post.html', {'form': post})

def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post = PostForm(request.POST, instance=post)
        if post.is_valid():
            post.save()
            return redirect('home')

    return render(request, 'add_post.html', {'form': post_form})

def delete_post(request, id):
    Post.objects.get(pk=id).delete()
    return redirect('home')