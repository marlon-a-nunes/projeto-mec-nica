from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=11, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.first_name
    
class Car(models.Model):
    CHOICE_BOARD = (
        ('mercosur', 'Mercosur'),
        ('old pattern', 'Old Pattern'),
    )
    
    car = models.CharField( max_length=50)
    car_year = models.CharField(max_length=4)
    type_of_board = models.CharField(max_length=11, choices=CHOICE_BOARD, null=True)
    board = models.CharField(max_length=10, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name = 'cars')
    created_at = models.DateTimeField(auto_now_add=True,  null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    
    
    def __str__(self):
        return self.car

class Service(models.Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    
    service = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='services')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.service
    
class Parts(models.Model):
    name_parts = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    parts_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='parts')
    
    def __str__(self):
        return self.name_parts
    