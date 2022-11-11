from datetime import datetime
from datetime import date
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

MIESIACE = (
        ('1', 'styczeń'),
        ('2', 'luty'),
        ('3', 'marzec'),
        ('4', 'kwiecień'),
        ('5', 'maj'),
        ('6', 'czerwiec'),
        ('7', 'lipiec'),
        ('8', 'sierpień'),
        ('9', 'wrzesień'),
        ('10', 'październik'),
        ('11', 'listopad'),
        ('12', 'grudzień'),
    )


class Osoba(models.Model):
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    miesiac_urodzenia = models.CharField(max_length=255, choices=MIESIACE, default=date.today().month)
    miesiac_dodania = models.CharField(max_length=255, choices=MIESIACE, default=date.today().month)
    data_dodania = models.DateField(default = datetime.now)
    druzyna = models.ForeignKey('Druzyna', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['nazwisko']

    def __str__ (self):
        return self.imie + ' ' + self.nazwisko

class Druzyna(models.Model):
    nazwa = models.CharField(max_length=255)
    kraj = models.CharField(max_length=2, validators=[RegexValidator('^[A-Z]', 'Tylko duże litery')])

    def __str__(self):
        return self.nazwa + ' ('+self.kraj+')'