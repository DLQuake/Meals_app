# Lab 3 - Zadanie 11

## 1. Wyświetl wszystkie obiekty modelu Osoba,

```python
>>> from osoby.models import Osoba
>>> Osoba.objects.all()

<QuerySet [<Osoba: Dominik Lewczyński>, <Osoba: Jan Mazur>, <Osoba: Marek Nowak>]>
```
## 2. Wyświetl obiekt modelu Osoba z id = 3,

```python
>>> from osoby.models import Osoba
>>> Osoba.objects.get(id=3)

<Osoba: Jan Mazur>
```

## 3. Wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik),

```python
>>> from osoby.models import Osoba
>>> Osoba.objects.filter(imie__startswith='D')

<QuerySet [<Osoba: Dominik Lewczyński>]>
```

## 4. Wyświetl unikalną listę drużyn przypisanych dla modeli Osoba,

```python
>>> from osoby.models import Osoba
>>> Osoba.objects.values('druzyna').order_by('druzyna').distinct()

<QuerySet [{'druzyna': 1}, {'druzyna': 2}, {'druzyna': 3}]>
```

## 5. Wyświetl nazwy drużyn posortowane alfabetycznie malejąco,

```python
>>> from osoby.models import Druzyna
>>> Druzyna.objects.all().order_by('-nazwa')

<QuerySet [<Druzyna: Tigers (US)>, <Druzyna: Legia warszawa (PL)>, <Druzyna: FC Barcelona (DE)>]>
```

## 6. Dodaj nową instancję obiektu klasy Osoba

```python
>>> from osoby.models import Osoba
>>> from django.utils import timezone
>>> o = Osoba(imie='Amadeusz', nazwisko='Mozart', miesiac_urodzenia=7, data_dodania=timezone.now())
>>> o.save()
```