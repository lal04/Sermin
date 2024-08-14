from django.contrib import admin
from django.urls import path,include
from .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('carro/',include('ControlVehiculos.url.carurls')),
    path('document/',include('ControlVehiculos.url.documenturls')),
    path('maintenance/',include('ControlVehiculos.url.maintenanceurls')),
    path('route/',include('ControlVehiculos.url.routeurls')),
    path('city/',include('ControlVehiculos.url.cityurls')),
    path('expense/',include('ControlVehiculos.url.expenseurls')),
]

