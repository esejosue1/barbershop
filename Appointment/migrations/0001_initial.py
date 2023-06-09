# Generated by Django 4.1.7 on 2023-03-25 16:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barbers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('is_closed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Business hours',
            },
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('service', models.CharField(default='Hair Cut', max_length=50)),
                ('date', models.DateTimeField()),
                ('time', models.CharField(choices=[('10 AM', '10 AM'), ('11 AM', '11 AM'), ('12 PM', '12 PM'), ('1 PM', '1 PM'), ('2 PM', '2 PM'), ('3 PM', '3 PM'), ('4 PM', '4 PM'), ('5 PM', '5 PM'), ('6 PM', '6 PM'), ('7 PM', '7 PM')], default='3 PM', max_length=10)),
                ('note', models.TextField(blank=True, max_length=500)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('barber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='barbers.barbers')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointmets',
            },
        ),
    ]
