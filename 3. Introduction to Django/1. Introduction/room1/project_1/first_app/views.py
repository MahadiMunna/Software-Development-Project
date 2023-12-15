from django.shortcuts import render
from django.http import HttpResponse	
# Create your views here.
def home(request):
    return HttpResponse("This page from first app")
def courses(request):
    return HttpResponse("This page from first app/courses")
