from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfile
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def home(request):
    return render(request,'home.html')

def userlogin(request):
    if request.user.is_authenticated:
        return redirect ('profile')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username = name, password = password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')

        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect ('profile')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account cretaed successfully')
                form.save(commit=True)
                print(form.cleaned_data)
        else:
            form = RegisterForm()        

        return render(request,'signup.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html', {'user':request.user})
    else:
        return redirect('login')

def userlogout(request):
    logout(request)
    return redirect('login')

def changePass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request,'Password has been changed')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form  = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form': form})
    else:
        return redirect('signup')

def changePass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                messages.success(request,'Password has been changed')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form  = SetPasswordForm(user=request.user)
        return render(request, 'changepass.html', {'form': form})
    else:
        return redirect('signup')
    
def editProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfile(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request,'Account updated successfully')
                form.save(commit=True)
                return redirect('profile')
        else:
            form = EditProfile(instance=request.user)        

        return render(request,'editProfile.html', {'form': form})
    else:
        return redirect('signup')