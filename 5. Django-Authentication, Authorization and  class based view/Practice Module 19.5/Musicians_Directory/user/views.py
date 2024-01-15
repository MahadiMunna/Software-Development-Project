from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import logout
from django.urls import reverse_lazy


# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account created successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'form.html', {'form': register_form, 'type':'Register'})

class UserLoginView(LoginView):
    template_name = 'form.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'User Information is incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
