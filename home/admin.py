from django.contrib import admin

# Register your models here.
from .models import Job, Education, JobSummary, Tech
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(JobSummary)
admin.site.register(Tech)

