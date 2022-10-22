from django.contrib import admin
from .models import Druzyna, Osoba

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', "data_dodania", 'kraj']
class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'kraj']

admin.site.register(Osoba, Admin)
admin.site.register(Druzyna, DruzynaAdmin)