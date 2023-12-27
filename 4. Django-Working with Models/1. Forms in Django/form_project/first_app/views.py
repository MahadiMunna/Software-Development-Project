from django.shortcuts import render
from . forms import ContactForm, StudentForm, PasswordValidator

# Create your views here.
def form(request):
    return render(request, 'form.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name, 'email': email, 'select':select})
    else:
        return render(request, 'about.html')

def djangoForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, 'django_form.html', {'form':form})
    else:
        form = ContactForm()
    return render(request, 'django_form.html', {'form':form})
def studentForm(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,  request.FILES, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'django_form.html',{'form':form})
def passwordForm(request):
    if request.method == 'POST':
        form = PasswordValidator(request.POST,  request.FILES, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidator()
    return render(request, 'django_form.html',{'form':form})