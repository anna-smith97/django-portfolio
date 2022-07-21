from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Job(models.Model):
    title = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    summary = models.CharField(max_length=1000, null=True)
    tech = models.CharField(max_length=100, null=True)
