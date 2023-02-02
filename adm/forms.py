from adm.models import Client, Car
from adm.models import Service, Parts
from django.forms import ModelForm


class Newclient(ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'phone_number', 'cpf', 'address')
        
class Newcar(ModelForm):
    class Meta:
        model = Car
        fields = ('car', 'car_year', 'type_of_board', 'board')

    
class Newservice(ModelForm):
    class Meta:
        model = Service
        fields = ('service', 'description', 'status', 'service_price',)
        
class Newparts(ModelForm):
    class Meta:
        model = Parts
        fields = ('name_parts', 'serial_number', 'parts_price')
        
