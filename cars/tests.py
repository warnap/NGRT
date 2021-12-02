import pytest

from .models import Car, Make, Rate
from .factories import *

headers = {"Content-Type": "application/json;charset=UTF-8"}


@pytest.mark.django_db
class TestCar:
    def test_create_car(self, client) -> None:
        assert Car.objects.count() == 0
        car: Car = CarFactory()

        assert Car.objects.count() == 1

        response = client.post('/cars/', {'make': 'volvo', 'model': 's60'}, headers=headers)

        assert response.status_code == 201
        assert Car.objects.count() == 2
        assert response.json() == {'id': 2, 'make': 'volvo', 'model': 'S60'}

    def test_create_empty_car(self, client) -> None:
        assert Car.objects.count() == 0

        json_response = {
            "make": [
                "This field is required."
            ],
            "model": [
                "This field is required."
            ]
        }

        response = client.post('/cars/', headers=headers)

        assert response.status_code == 400

        assert response.json() == json_response

    def test_delete_car(self, client) -> None:
        assert Car.objects.count() == 0
        car: Car = CarFactory()

        assert Car.objects.count() == 1

        # response = client.delete('/cars/{}'.format(car.pk))
        #
        # assert response.status_code == 301
        # # print(response.json())
        # assert Car.objects.count() == 0

    def test_list_of_cars(self, client) -> None:
        assert Car.objects.count() == 0
        car: Car = CarFactory()
        # car1: Car = CarFactory(make='volvo', model='S60')

        response = client.get('/cars/')

        assert response.status_code == 200


@pytest.mark.django_db
class TestRate:
    def test_create_rate(self, client) -> None:
        assert Rate.objects.count() == 0
        rate: Rate = RateFactory()

        assert Rate.objects.count() == 1

        # response = client.post('/rat/', {'make': 'volvo', 'model': 's60'})
        #
        # assert response.status_code == 201
        # assert Car.objects.count() == 2
        # assert response.json() == {'id': 2, 'make': 'VOLVO', 'model': 'S60'}
