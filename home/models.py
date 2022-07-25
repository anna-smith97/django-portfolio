from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

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
    class Meta:
        verbose_name_plural = "Education"


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

    def __str__(self):
        return f"{self.school}"




class Job(models.Model):
    class Meta:
        verbose_name_plural = "Job"


    title = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
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
    tech = models.ManyToManyField('Tech')


    def __str__(self):
        return f"{self.title} at {self.company}"

    def __repr__(self):
        return {
            'title':self.title, 
            'company':self.company,
            'start':self.start_date,
            'end':self.end_date,
            'city':self.city,
            'state':self.state,
            'current':self.current,
            'tech':self.tech
            }


class Tech(models.Model):
    class Meta:
        verbose_name_plural = "Tech"

    name = models.CharField(max_length=200, null=True)
    proficiency = models.IntegerField(
        default=1, 
        validators=[MaxValueValidator(10),MinValueValidator(1)])

    def __str__(self):
        return f"{self.name}"



class JobSummary(models.Model):
    class Meta:
        verbose_name_plural = "Job Summary"


    job = models.ForeignKey("Job", on_delete=models.SET_NULL, null=True)
    task = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.task


