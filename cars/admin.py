from django.contrib import admin

from cars.models import CarModel


@admin.register(CarModel)
class CarsModelAdmin(admin.ModelAdmin):
    list_display = ['model', 'obyom2', 'moshnost2', 'korobka', 'dvigatel', 'toplivo']
    list_filter = ['obyom2', 'moshnost2', 'korobka', 'dvigatel', 'toplivo']
    search_fields = ['model', 'obyom2', 'moshnost2', 'korobka', 'dvigatel', 'toplivo']
