from django.contrib import admin
from .models import Car, Rate, Make


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass
