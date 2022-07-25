from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneralContext, Job, JobSummary
from datetime import date

gc = GeneralContext()

def index(request):
    gc.links['Home']['status'] = "is-active"
    gc.links['Experience']['status'] = "not-active"
    context = {
        "title": gc.title, 
        "herotitle": gc.herotitle,
        "herosubtitle": gc.herosubtitle,
        "links": gc.links
        }

    tiles = {'LinkedIn': {'field': 'LinkedIn', 'icon': 'fa-brands fa-linkedin', 'link': 'https://www.linkedin.com/in/annasmith60/'},
             'Github': {'field': 'GitHub', 'icon': 'fa-brands fa-github', 'link': 'https://github.com/anna-smith97/'},
             'Resume': {'field': 'Resume', 'icon': 'fa-solid fa-folder', 'link': '/'},
             'Email': {'field': 'Email', 'icon': 'fa-solid fa-envelope', 'link': 'mailto:annaleighsmith60@gmail.com'}
             }

    context['tiles'] = tiles
    gc.links['Home']['status'] = "not-active"
    gc.links['Experience']['status'] = "is-active"


    job_obj = Job.objects.all()
    jobs_dict = {}
    job_summary_list = []
    i = 0
    for j in job_obj:
        i +=1
        job_obj_values = j.__repr__()
        if job_obj_values['current'] == True:
            job_obj_values['end'] = "Current"
            
        jobs_dict[i] = job_obj_values
        summary_obj = JobSummary.objects.filter(job_id=j.id).all()
        for s in summary_obj:
            job_summary_list.append(str(s))
        
        jobs_dict[i]['tasks'] = job_summary_list

    
    context['myjobs'] = jobs_dict

    return render(request, "index.html", context)


def jobs(request):
    gc.links['Home']['status'] = "not-active"
    gc.links['Experience']['status'] = "is-active"
    context = {
        "title": gc.title, 
        "herotitle": gc.herotitle,
        "herosubtitle": gc.herosubtitle,
        "links": gc.links
        }

    job_obj = Job.objects.all()
    jobs_dict = {}
    job_summary_list = []
    i = 0
    for j in job_obj:
        i +=1
        job_obj_values = j.__repr__()
        if job_obj_values['current'] == True:
            job_obj_values['end'] = "Current"
            
        jobs_dict[i] = job_obj_values
        summary_obj = JobSummary.objects.filter(job_id=j.id).all()
        for s in summary_obj:
            job_summary_list.append(str(s))
        
        jobs_dict[i]['tasks'] = job_summary_list

    
    context['myjobs'] = jobs_dict

    return render(request, "jobs.html", context)




