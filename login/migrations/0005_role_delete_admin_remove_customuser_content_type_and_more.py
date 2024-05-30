# Generated by Django 5.0.6 on 2024-05-30 16:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Admin', 'Admin'), ('Support', 'Support'), ('Developer', 'Developer'), ('OnlyAgent', 'OnlyAgent')], default='OnlyAgent', max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='Developer',
        ),
        migrations.DeleteModel(
            name='Support',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
