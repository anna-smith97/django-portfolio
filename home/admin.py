from django.contrib import admin

# Register your models here.
from .models import Job, Education, JobSummary, Tech
from django.apps import apps

admin.site.register(Education)
admin.site.register(Tech)


admin.site.register(JobSummary)



class JobSummaryInline(admin.TabularInline):
    model = JobSummary

class JobAdmin(admin.ModelAdmin):
    inlines = (JobSummaryInline, )

admin.site.register(Job, JobAdmin)

