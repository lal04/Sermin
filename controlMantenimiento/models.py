from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from decimal import Decimal



class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField(verbose_name="año")
    numero_placa = models.CharField(max_length=20, unique=True, verbose_name='numero de placa')
    def __str__(self):
        return self.marca
    
class HistorialKilometraje(models.Model):
    TIPO_CHOICES=(
        (('Salida'), ('Salida')),
        (('Entrada'), ('Entrada'))
        )
    
    vehiculo=models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
    fecha=models.DateField(default=now)
    tipo=models.CharField(max_length=15, choices=TIPO_CHOICES, default='Salida')
    kilometraje=models.IntegerField()
    
    
class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=100)
    kilometraje_promedio=models.IntegerField(default=5000)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
    
class Proveedor(models.Model):
    nombre=models.CharField(max_length=100, null=False, blank=False)
    ruc=models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Mantenimiento(models.Model):
    ESTADOS_CHOICES=(
        ('Pendiente','Pendiente' ),
        ('Atendido','Atendido' ),
    )
    
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True) ###el null solo fue para poder crear la migracion
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE)
    fecha_mantenimiento = models.DateField(default=now)
    kilometraje=models.IntegerField(null=True)
    kilometraje_proximo_mantenimiento=models.IntegerField(null=True, blank=True, default=0)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.CharField(choices=ESTADOS_CHOICES, default='Pendiente', max_length=15)
    descripcion = models.TextField(blank=True, null=True)
    
    def save(self,*args, **kwargs):
        self.costo = round(Decimal(self.costo), 2)
        self.kilometraje_proximo_mantenimiento=self.kilometraje+self.tipo_mantenimiento.kilometraje_promedio
        return super().save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.vehiculo} - {self.tipo_mantenimiento} ({self.kilometraje_proximo_mantenimiento} km)"
    
    
    
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
    ESTADOS_CHOICES=(
        ('Pendiente','Pendiente' ),
        ('Tramitado','Tramitado' ),
    )
    tipo_documento = models.CharField(max_length=50, choices=TIPO_DOCUMENTO_CHOICES, verbose_name='tipo de documento')

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fecha_emision = models.DateField(default=now,verbose_name='fecha de emision')
    fecha_expiracion = models.DateField(verbose_name='fecha de expiracion')
    estado=models.CharField(choices=ESTADOS_CHOICES, default='Pendiente', max_length=15)
    
    def __str__(self):
        return f"{self.get_tipo_documento_display()} - {self.fecha_emision}"


    
