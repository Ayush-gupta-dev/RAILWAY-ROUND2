# Generated by Django 5.0.1 on 2024-01-11 16:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_station_halt_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='fare_1ac',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='train',
            name='fare_2ac',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='train',
            name='fare_3ac',
            field=models.IntegerField(default=200, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='train',
            name='total_seats_1ac',
            field=models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='train',
            name='total_seats_2ac',
            field=models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='train',
            name='total_seats_3ac',
            field=models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
