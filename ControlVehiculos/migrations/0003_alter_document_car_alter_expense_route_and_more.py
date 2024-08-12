# Generated by Django 5.0.7 on 2024-07-29 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlVehiculos', '0002_alter_route_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='ControlVehiculos.car'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='ControlVehiculos.route'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance', to='ControlVehiculos.car'),
        ),
        migrations.AlterField(
            model_name='route',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes_car', to='ControlVehiculos.car'),
        ),
        migrations.AlterField(
            model_name='route',
            name='ciudad_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_cities', to='ControlVehiculos.city'),
        ),
        migrations.AlterField(
            model_name='route',
            name='ciudad_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_cities', to='ControlVehiculos.city'),
        ),
    ]
