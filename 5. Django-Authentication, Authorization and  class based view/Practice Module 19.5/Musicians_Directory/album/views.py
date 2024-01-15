from django.shortcuts import render,redirect
from .forms import AlbumForm
from .models import Album
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddAlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add'
        return context

@method_decorator(login_required, name='dispatch')
class UpdateAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit'
        return context

@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    