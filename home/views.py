from django.shortcuts import render
from django.http import HttpResponse

from .models import Job, Greeting, JobSummary
from datetime import date
# Create your views here.
def index(request):
    context = {
        "title": "Portfolio - Anna Smith", 
        "herotitle": "Hi, I'm Anna",
        "herosubtitle": "python development, data engineering, & more",
        "links": [
            ['home','is-active','/'],
            # ['projects','not-active','/projects'],
            ['experience','not-active','/experience']
            ]
        }
    context['tiles'] = {
        "tiles": [
            {'field': 'LinkedIn','icon':'fa-brands fa-linkedin', 'link':'/'},
            {'field': 'GitHub','icon':'fa-brands fa-github', 'link':'https://github.com/anna-smith97/'},
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
    # ['projects','not-active','/projects'],
    ['experience','is-active','/experience']
    ]
    }

    job_obj = Job.objects.all()
    jobs_dict = {}
    jobs_list = []
    
    for j in job_obj:

        if j.end_date is None and j.current is True:
            j.end_date = "Current"
        else:
            if j.end_date is None:
                j.end_date = ""
            else:
                j.end_date = j.end_date.strftime("%B %Y")

        jobs_dict[j.id] = {
            'title':j.title,
            'company':j.company,
            'city': j.city,
            'state': j.state,
            'tech':j.tech,
            'start':j.start_date.strftime("%B %Y"),
            'end':j.end_date,
            'tasks':[]
            }
        summary_obj = JobSummary.objects.filter(job_id=j.id).all()
        for s in summary_obj:
            jobs_dict[j.id]['tasks'].append(s.task)
        
        jobs_list.append(jobs_dict[j.id])
    context['myjobs'] = jobs_list
 
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


