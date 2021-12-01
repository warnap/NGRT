import requests.exceptions
from rest_framework import serializers
from .models import Make, Car, Rate
from .externalAPI import get_make_and_models
from django.core.exceptions import ObjectDoesNotExist


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = ['name']


class RateSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField()
    rating = serializers.IntegerField(source='rate')

    class Meta:
        model = Rate
        fields = ['car_id', 'rating']

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


class CarListSerializer(serializers.ModelSerializer):
    make = serializers.CharField(required=True)
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def validate(self, data):
        validate_make = data['make']
        validate_model = data['model']
        db_make = None
        new_model = None
        try:
            makeApi, models = get_make_and_models(str(validate_make).lower())

            if makeApi is None:
                raise serializers.ValidationError({'make': "Make doesn't not exist in External API"})

            if models:
                try:
                    db_make = Make.objects.get(name__iexact=makeApi)
                except ObjectDoesNotExist:
                    db_make = Make.objects.create(name=makeApi)

                for model in models:
                    if validate_model.lower() == model.lower():
                        new_model = model
                        break

        except requests.exceptions.ConnectionError:
            raise serializers.ValidationError({'connection': 'External API connection error'})

        if new_model:
            db_make.save()
            data['make'] = db_make.name
            data['model'] = new_model

            return data
        else:
            raise serializers.ValidationError({'model': "Model doesn't not exist in External API"})

    def create(self, validated_data):
        make_name = validated_data['make']
        model = validated_data['model']
        make = Make.objects.get(name__iexact=make_name)
        car = Car.objects.create(make=make, model=model)
        car.save()
        return car


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
