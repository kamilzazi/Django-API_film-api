from rest_framework import serializers
from .models import Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'plakat']

class FilmFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'tytul', 'opis', 'rok', 'plakat']