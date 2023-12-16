from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'navigation/about.html')

def contact(request):
    d = {'author':'Mahadi Hasan Munna','age':15,'lst':['a','b','c'],'courses':[
        {
        'id':1,
        'name':'Python',
        'fee':1000
        },
        {
        'id':2,
        'name':'C',
        'fee':1200
        },
        {
        'id':3,
        'name':'Django',
        'fee':1500
        }
    ]}
    return render(request, 'navigation/contact.html',d)