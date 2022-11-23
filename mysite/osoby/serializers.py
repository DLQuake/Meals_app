from datetime import date
from rest_framework import serializers
from .models import MIESIACE, Osoba, Druzyna

class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_urodzenia = serializers.ChoiceField(choices=MIESIACE, default=MIESIACE[0][0])
    kraj  = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all())

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.kraj  = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance

    def validate_miesiac_dodania(self, value):
        if value > str(date.today().month):
            raise serializers.ValidationError(
                "Miesiac dodania, nie moze byc przyszly!",
            )
        return value

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Imie musi sie składać tylko z liter!",
            )
        return value

class DruzynaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    kraj = serializers.CharField(required=True)
    nazwa = serializers.CharField(required=True)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.save()
        return instance