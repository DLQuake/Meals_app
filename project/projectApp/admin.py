from django.contrib import admin
from .models import Project

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['id','name','name', 'instructions', 'region', 'slug', 'image_url']

admin.site.register(Project, Admin)