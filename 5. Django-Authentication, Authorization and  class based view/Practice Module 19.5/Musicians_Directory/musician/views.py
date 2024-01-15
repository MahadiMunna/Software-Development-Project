from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddMusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Add'
        return context

@method_decorator(login_required, name='dispatch')
class UpdateMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit'
        return context