from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        post = PostForm(request.POST)
        if post.is_valid():
            post.instance.author = request.user
            post.save()
            return redirect('home')
    else:
        post = PostForm()
    return render(request, 'add_post.html', {'form': post, 'type':'Add'})

@login_required
def edit_post(request, id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post = PostForm(request.POST, instance=post)
        if post.is_valid():
            post.instance.author = request.user
            post.save()
            return redirect('home')

    return render(request, 'add_post.html', {'form': post_form, 'type':'Edit'})

@login_required
def delete_post(request, id):
    Post.objects.get(pk=id).delete()
    return redirect('home')