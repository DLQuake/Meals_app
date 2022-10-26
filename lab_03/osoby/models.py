from datetime import datetime
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Osoba(models.Model):
    class Miesiace(models.IntegerChoices):
        Styczeń = 1
        Luty = 2
        Marzec = 3
        Kwiecień = 4
        Maj = 5
        Czerwiec = 6
        Lipiec = 7
        Sierpień = 8
        Wrzesień = 9
        Październik = 10
        Listopad = 11
        Grudzień = 12

    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    miesiac_urodzenia  = models.IntegerField(choices=Miesiace.choices, default=Miesiace.choices[0])
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