# Generated by Django 4.1.7 on 2023-03-21 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesshours',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
