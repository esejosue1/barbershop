# Generated by Django 4.1.7 on 2023-03-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0002_alter_barbers_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbers',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
