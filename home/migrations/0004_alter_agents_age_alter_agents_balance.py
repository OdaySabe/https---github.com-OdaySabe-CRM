# Generated by Django 5.0.6 on 2024-05-30 09:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='agents',
            name='balance',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
