from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    modelo=models.CharField(max_length=20)
    placa=models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.modelo

class Document(models.Model):
    tipo=models.CharField(max_length=20)
    fecha_inicio=models.DateField()
    fecha_vencimiento=models.DateField()
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='documents', verbose_name='carro')
    
    def __str__(self) -> str:
        return self.tipo
    
class Maintenance(models.Model):
    titulo=models.CharField(max_length=20)
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenance')
    fecha_mantenimiento=models.DateTimeField()
    kilometraje=models.IntegerField()
    monto=models.IntegerField()
    
    def __str__(self) -> str:
        return self.titulo
class City(models.Model):
    nombre=models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.nombre
    
class Route(models.Model):
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    car=models.ForeignKey(Car, on_delete=models.CASCADE, related_name='routes_car', verbose_name="Carro")
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='routs', verbose_name="Usuario")
    kilometraje_inicio=models.IntegerField()
    kilometraje_fin=models.IntegerField()
    ciudad_origen=models.ForeignKey(City, on_delete=models.CASCADE, related_name='origin_cities')
    ciudad_destino=models.ForeignKey(City, on_delete=models.CASCADE, related_name='destination_cities')
    def __str__(self) -> str:
        return str(self.id)
class Expense(models.Model):  
    titulo=models.CharField(max_length=20)
    route=models.ForeignKey(Route, on_delete=models.CASCADE, related_name='routes', verbose_name='ruta')
    descripcion=models.TextField()
    monto=models.IntegerField()
    def __str__(self) -> str:
        return self.titulo
    
    


