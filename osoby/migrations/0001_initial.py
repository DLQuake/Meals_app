# Generated by Django 4.1.2 on 2022-10-19 17:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
                ('miesiac_urodzenia', models.IntegerField(choices=[(1, 'Styczeń'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecień'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpień'), (9, 'Wrzesień'), (10, 'Październik'), (11, 'Listopad'), (12, 'Grudzień')], default=(1, 'Styczeń'))),
                ('data_dodania', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ['nazwisko'],
            },
        ),
    ]
