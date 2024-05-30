# Generated by Django 5.0.6 on 2024-05-30 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_agents_age_alter_agents_balance'),
        ('login', '0005_role_delete_admin_remove_customuser_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agents',
            name='role',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.role', verbose_name='user_role'),
        ),
    ]
