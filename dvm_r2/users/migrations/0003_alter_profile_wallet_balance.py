# Generated by Django 5.0.1 on 2024-01-06 19:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_wallet_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='wallet_balance',
            field=models.DecimalField(decimal_places=0, default=50, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
