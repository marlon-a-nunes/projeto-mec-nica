from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('listclient/', views.listClient, name="list-client"),
    path('car/<int:id>', views.cardetail, name="car-detail"),
    path('newclient/', views.newclient, name = 'new-client'),
    path('teste/', views.teste, name='teste' ),
 
]
