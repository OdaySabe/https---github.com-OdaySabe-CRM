# Generated by Django 5.0.6 on 2024-05-29 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('balance', models.FloatField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
