from django.shortcuts import render
from django.http import HttpResponse

from .models import Job, Greeting

# Create your views here.
def index(request):
    context = {
        "title": "Portfolio - Anna Smith", 
        "herotitle": "Hi, I'm Anna",
        "herosubtitle": "python develpment, data engineering, & more",
        "links": [
            ['home','is-active','/'],
            ['projects','not-active','/projects'],
            ['experience','not-active','/experience']
            ]
        }
    context['tiles'] = {
        "tiles": [
            # {'field': 'Miami, FL','icon':'fa-solid fa-map-pin','link':'/'},
            # {'field': 'Twenty-Five','icon':'fa-solid fa-baby', 'link':'/'},
            {'field': 'LinkedIn','icon':'fa-brands fa-linkedin', 'link':'/'},
            {'field': 'GitHub','icon':'fa-brands fa-github', 'link':'/'},
            {'field': 'Resume','icon':'fa-solid fa-folder', 'link':'/'},
            {'field': 'Email','icon':'fa-solid fa-envelope', 'link':'/'}
        ]
        }
    return render(request, "index.html", context)


def jobs(request):
    context = {
    "title": "Portfolio - Anna Smith", 
    "herotitle": "Hi, I'm Anna",
    "herosubtitle": "python develpment, data engineering, & more",
    "links": [
    ['home','not-active','/'],
    ['projects','not-active','/projects'],
    ['experience','is-active','/experience']
    ]
    }
    myjobs = Job.objects.all().values()
  
    jobs_dict = []
    i = 0
    for x in myjobs:
        jobs_dict += [
            [x['title'], x['company'], x['summary'], x['tech']]
            ]
        i = i + 1
    context['myjobs'] = jobs_dict
    return render(request, "jobs.html", context)

def db(request):
    context = {
        "title": "Portfolio - Anna Smith", 
        "herotitle": "Hi, I'm Anna",
        "herosubtitle": "python develpment, data engineering, & more"
        }
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    context["greetings"] = greetings

    return render(request, "db.html", context)
