from rest_framework import serializers
from .models import Make, Car, Rate
from django.core.exceptions import ObjectDoesNotExist


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['name']


class RateSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField()
    rating = serializers.IntegerField(source='rate')

    def validate_car_id(self, value):
        try:
            Car.objects.get(id=value)
        except ObjectDoesNotExist:
            raise serializers.ValidationError('Invalid car_id: ObjectDoesNotExist')

        return value

    def validate_rating(self, value):
        if value not in range(1, 6):
            raise serializers.ValidationError('Invalid rating (Can use only 1-5)')

        return value

    def create(self, validated_data):
        return Rate.objects.create(**validated_data)

    class Meta:
        model = Rate
        fields = ['car_id', 'rating']


class CarCreateSerializer(serializers.ModelSerializer):
    make = serializers.StringRelatedField(many=False)

    class Meta:
        model = Car
        fields = ['make', 'model']

    def create(self, validated_data):
        return Car.objects.create(**validated_data)


class CarListSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())
    avg_rating = serializers.FloatField(read_only=True)

    # TODO: Create fields validation and checking make and models on external api

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']


class CarAddSerializer(serializers.ModelSerializer):
    make = serializers.StringRelatedField(many=False)

    class Meta:
        model = Car
        fields = ['make', 'model']


class CarDetailSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())

    class Meta:
        model = Car
        fields = ['make', 'model']


class PopularCarListSerializer(serializers.ModelSerializer):
    make = serializers.StringRelatedField(many=False)
    rates_number = serializers.IntegerField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']
