from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Make(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = [['make', 'model']]

    def __str__(self):
        return '{}-{}'.format(self.make, self.model)


class Rate(models.Model):
    DEFAULT_CAR_ID = 1
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=DEFAULT_CAR_ID)
    rate = models.PositiveIntegerField(choices=RATING_CHOICES,
                                       default=1,
                                       validators=[
                                           MaxValueValidator,
                                           MinValueValidator
                                       ])

    def __str__(self):
        return '{}-{}'.format(self.car, str(self.rate))
