# import api
from rest_framework import serializers
from .models import Make, Car, Rate


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['id', 'name']


class CarSerializer(serializers.ModelSerializer):
    make = Make.objects.all()

    class Meta:
        model = Car
        fields = []


class CarListSerializer(serializers.ModelSerializer):
    make = Make.objects.all()

    class Meta:
        model = Car
        fields = ['make', 'model']


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = []
