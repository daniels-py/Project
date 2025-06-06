# Generated by Django 5.2 on 2025-04-08 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidades', models.PositiveIntegerField(default=0, verbose_name='Unidades en inventario')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='products.producto')),
            ],
        ),
    ]
