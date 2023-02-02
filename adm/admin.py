from django.contrib import admin
from .models import Client
from .models import Parts
from .models import Service
from .models import Car

class Adm(admin.ModelAdmin):
    list_display = ('first_name', 'cpf', 'address', 'created_at')
    search_fields = ['cpf']

admin.site.register(Client, Adm)

class admCar(admin.ModelAdmin):
    list_display = ('car', 'car_year', 'board' )
    search_fields = ['board']
admin.site.register(Car, admCar)

class admService(admin.ModelAdmin):
    list_display = ('service', 'status', 'service_price', 'car')
    search_fields = ['status']
    
admin.site.register(Service, admService)

class admParts(admin.ModelAdmin):
    list_display = ('name_parts', 'serial_number', 'parts_price', 'car')
    search_fields = ['name_parts']
    
admin.site.register(Parts, admParts)