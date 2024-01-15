from typing import Any
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
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


from django.utils.decorators import method_decorator
# Add post using class based view
from django.views.generic import CreateView
from django.urls import reverse_lazy

@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# Update post using class based view
from django.views.generic import UpdateView
@method_decorator(login_required, name='dispatch')
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

# Delete post using class based view
from django.views.generic import DeleteView
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

from django.views.generic import DetailView
class DetailPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context