from django.contrib import admin

from cars.models import CarModel


@admin.register(CarModel)
class CarsModelAdmin(admin.ModelAdmin):
    list_display = ['model', 'obyom', 'moshnost', 'korobka', 'dvigatel', 'toplivo']
    list_filter = ['obyom', 'moshnost', 'korobka', 'dvigatel', 'toplivo']
    search_fields = ['model', 'obyom', 'moshnost', 'korobka', 'dvigatel', 'toplivo']
