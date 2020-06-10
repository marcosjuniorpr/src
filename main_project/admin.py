from django.contrib import admin
from main_project.models import Report, Blog, ContactForm
# Register your models here.

admin.site.register([Report, Blog, ContactForm])