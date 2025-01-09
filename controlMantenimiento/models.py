from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta



class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField(verbose_name="año")
    numero_placa = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.marca
    
    
class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
    
class Proveedor(models.Model):
    nombre=models.CharField(max_length=100, null=False, blank=False)
    ruc=models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Mantenimiento(models.Model):
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True) ###el null solo fue para poder crear la migracion
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField(default=date.today)
    fecha_proximo_mantenimiento = models.DateField(default=lambda:date.today() + relativedelta(months=1))
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehiculo} - {self.tipo_mantenimiento} ({self.fecha_mantenimiento})"
    
    
    
class Documento(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('Tarjeta de Circulacion', 'Tarjeta de Circulacion'),
        ('Licencia de Conducir', 'Licencia de Conducir'),
        ('Soat', 'Soat'),
        ('Tarjeta de Propiedad', 'Tarjeta de Propiedad'),
        ('Revision Tecnica', 'Revision Tecnica'),
        ('Permiso de Recojo de Reciduos', 'Permiso de Recojo de Reciduos'),
        ('Certificado de Aptitud Psicofisica', 'Certificado de Aptitud Psicofisica'),
        ('Capacitacion', 'Capacitacion'),
        ('Otro', 'Otro'),
        
        # Agrega más tipos de documentos según sea necesario
    ]
    tipo_documento = models.CharField(max_length=50, choices=TIPO_DOCUMENTO_CHOICES)

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fecha_emision = models.DateField(default=date.today())
    fecha_expiracion = models.DateField(default=lambda: date.today() + relativedelta(years=5))
    
    def clean(self):
        super().clean()
        if self.fecha_emision >= self.fecha_expiracion:
            raise ValidationError("La fecha de emisión debe ser menor a la fecha de expiración.")
    
    def __str__(self):
        return f"{self.get_tipo_documento_display()} - {self.fecha_emision}"


    
