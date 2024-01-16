# Generated by Django 5.0.1 on 2024-01-16 06:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.CharField(max_length=10, unique=True)),
                ('train_name', models.CharField(max_length=100, unique=True)),
                ('from_station_code', models.CharField(max_length=50)),
                ('to_station_code', models.CharField(max_length=50)),
                ('train_available', models.BooleanField(default=True)),
                ('runs_on', models.CharField(max_length=20)),
                ('total_seats_1ac', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_seats_2ac', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_seats_3ac', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('fare_1ac', models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0)])),
                ('fare_2ac', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('fare_3ac', models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.CharField(default='', max_length=10)),
                ('station_code', models.CharField(max_length=100)),
                ('station_name', models.CharField(max_length=100)),
                ('distance', models.IntegerField()),
                ('arrival_time', models.TimeField()),
                ('halt_time', models.CharField(max_length=10)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.train')),
            ],
        ),
    ]
