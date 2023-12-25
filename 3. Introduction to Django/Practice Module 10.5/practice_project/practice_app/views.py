from django.shortcuts import render

# Create your views here.
def app_page(request):
    return render(request, 'app_page.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def same(request):
    return render(request, 'same_page.html')