from django.db import models
from django.utils import timezone

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

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


class JobSummary(models.Model):
    job = models.ForeignKey("Job", on_delete=models.SET_NULL, null=True)
    task = models.CharField(max_length=200, null=True)