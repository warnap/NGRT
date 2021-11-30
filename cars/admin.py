from django.contrib import admin
from .models import Car, Make, Rate


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model')


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'rate')
