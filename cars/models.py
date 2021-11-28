from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Make(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Rate(models.Model):
    rating = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5),
                    MinValueValidator(0)]
    )


class Car(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.CharField(max_length=100, unique=True)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['make', 'model']]
