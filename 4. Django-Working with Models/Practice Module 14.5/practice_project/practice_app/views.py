from django.shortcuts import render
from practice_app.forms import Practice_Form

# Create your views here.
def home(request):
    form = Practice_Form
    return render(request,'home.html', {'form':form})