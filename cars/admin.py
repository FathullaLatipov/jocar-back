from django.contrib import admin

from cars.models import CarModel


@admin.register(CarModel)
class CarsModelAdmin(admin.ModelAdmin):
    list_display = ['model', 'volume', 'power', 'transmission', 'engine', 'fuel']
    list_filter = ['volume', 'power', 'transmission', 'engine', 'fuel']
    search_fields = ['model', 'volume', 'power', 'transmission', 'engine', 'fuel']
