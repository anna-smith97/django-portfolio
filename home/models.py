from django.db import models
from django.utils import timezone

class GeneralContext:
    def __init__(self):
        self.title = "Portfolio - Anna Smith"
        self.herotitle = "Hi, I'm Anna"
        self.herosubtitle = "python development, data engineering, & more"
        self.links = {
            'Home':{'name':'home','status':'not-active','ref':'/'},
            'Experience':{'name':'digital resume','status':'not-active','ref':'/experience'}
        }


class Education(models.Model):
    school = models.CharField(max_length=100, null=True)
    major = models.CharField(max_length=100, null=True)
    start_date = models.DateField(
        auto_now = False,
        auto_now_add= False,
        null=True
    )
    end_date = models.DateField(
        auto_now = False,
        auto_now_add= False,
        null=True,
    )

class Job(models.Model):
    title = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    tech = models.CharField(max_length=100, null=True)
    start_date = models.DateField(
        auto_now = False,
        auto_now_add= False,
        null=True
    )
    end_date = models.DateField(
        auto_now = False,
        auto_now_add= False,
        null=True,

    )
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=2, null=True)
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __repr__(self):
        return {
            'title':self.title, 
            'company':self.company,
            'tech':self.tech,
            'start':self.start_date,
            'end':self.end_date,
            'city':self.city,
            'state':self.state,
            'current':self.current,
            }

class JobSummary(models.Model):
    job = models.ForeignKey("Job", on_delete=models.SET_NULL, null=True)
    task = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.task


