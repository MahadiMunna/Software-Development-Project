from django.shortcuts import render
import datetime

def home(request):
    dateToday = datetime.datetime.now()
    print(dateToday)
    posted = "2023-12-25 12:21:57.034065"
    data = {
        'userName': ['Mahadi','Hasan','Munna'],
        "nickname": "munna",
        "id": "203-15-3881",
        "date": dateToday,
        "height":5.4,
        "study":"",
        "laptop": 2,
        "favourite":["cycling","programimg","playing"],
        "friends": [{"name":"Sazid"},{"name":"Tamim"},{"name":"Zahin"},{"name":"Fahad"}],
        "msg": "Hello, I'm Munna. I'm a student of computer science",
        "post":posted,
    }
    return render(request, 'home.html', data)