# Generated by Django 5.0.6 on 2024-06-11 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20, unique=True)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo_local', models.CharField(max_length=100)),
                ('equipo_visitante', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cancha')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cliente')),
            ],
        ),
    ]
