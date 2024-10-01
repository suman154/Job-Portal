from django.contrib import admin
from .models import Job, Company, Application
# Register your models here.

admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Application)