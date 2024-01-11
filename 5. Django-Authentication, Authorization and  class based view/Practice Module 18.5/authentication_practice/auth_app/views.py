from django.shortcuts import render, redirect
from  . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login,  logout, update_session_auth_hash

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Successfully registered')
                form.save()
                return redirect('login')
        else:
            form = forms.RegisterForm()
        return render(request, 'form.html', {'form':form, 'type': 'Register'})
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = user_name, password = password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged In Successfully')
                    return redirect('profile')
                else:
                    messages.warning('Provide correct username and password')
                    return redirect('login')
        else:
            form = AuthenticationForm()
        return render(request, 'form.html', {'form':form, 'type': 'Login'})

def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('home')

def change_pass_with(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request,'Password changed successfully')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form  = PasswordChangeForm(user=request.user)
        return render(request, 'form.html', {'form': form, 'type': 'Change Password'})
    else:
        return redirect('register')

def change_pass_without(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request,'Password changed successfully')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form  = SetPasswordForm(user=request.user)
        return render(request, 'form.html', {'form': form, 'type': 'Change Password'})
    else:
        return redirect('signup')