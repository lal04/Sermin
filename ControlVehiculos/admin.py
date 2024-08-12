from django.contrib import admin
from . import models

admin.site.register(models.Car)
admin.site.register(models.City)
admin.site.register(models.Document)
admin.site.register(models.Maintenance)
admin.site.register(models.Route)
admin.site.register(models.Expense)