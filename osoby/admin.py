from django.contrib import admin

from osoby.models import Osoba

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'miesiac_urodzenia', "data_dodania"]

admin.site.register(Osoba, Admin)