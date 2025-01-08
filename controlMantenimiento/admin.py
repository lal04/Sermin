from django.contrib import admin
from .models import (Vehiculo,
                     TipoMantenimiento,
                     Mantenimiento,
                     Documento)

admin.site.register(Vehiculo)
admin.site.register(TipoMantenimiento)
admin.site.register(Mantenimiento)
admin.site.register(Documento)
