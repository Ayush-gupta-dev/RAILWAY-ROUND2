# Generated by Django 5.0.1 on 2024-01-05 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_train_runs_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_code', models.CharField(max_length=100)),
                ('station_name', models.CharField(max_length=100)),
                ('distance', models.IntegerField()),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('halt_time', models.TimeField()),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.train')),
            ],
        ),
    ]
