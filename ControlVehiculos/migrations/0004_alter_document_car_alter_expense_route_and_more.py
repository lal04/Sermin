# Generated by Django 5.0.7 on 2024-08-12 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlVehiculos', '0003_alter_document_car_alter_expense_route_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='ControlVehiculos.car', verbose_name='carro'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='ControlVehiculos.route', verbose_name='ruta'),
        ),
        migrations.AlterField(
            model_name='route',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes_car', to='ControlVehiculos.car', verbose_name='Carro'),
        ),
        migrations.AlterField(
            model_name='route',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routs', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
