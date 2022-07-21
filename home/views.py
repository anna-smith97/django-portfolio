from django.shortcuts import render
from django.http import HttpResponse

from .models import Job

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    context = {
        "title": "Portfolio - Anna Smith", 
        "herotitle": "Hi, I'm Anna",
        "herosubtitle": "python develpment, data engineering, & more"
        }

    return render(request, "index.html", context)


def jobs(request):
    myjobs = Job.objects.all().values()
    output = ""
    for x in myjobs:
        output += f"{x['title']}, {x['company']}<br>"
    return HttpResponse(output)