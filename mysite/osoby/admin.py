from django.contrib import admin
from .models import Druzyna, Osoba

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['id','wlasciciel','imie', 'nazwisko', 'miesiac_urodzenia', 'miesiac_dodania', 'data_dodania', 'kraj']
    list_filter = ['kraj', 'data_dodania']
class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa', 'kraj']
    list_filter = ['kraj']

admin.site.register(Osoba, Admin)
admin.site.register(Druzyna, DruzynaAdmin)