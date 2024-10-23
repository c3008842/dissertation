# Generated by Django 5.1.1 on 2024-10-23 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_email', models.EmailField(max_length=254)),
                ('secondary_email', models.EmailField(max_length=254)),
                ('optional1_email', models.EmailField(max_length=254)),
                ('optional2_email', models.EmailField(max_length=254)),
                ('optional3_email', models.EmailField(max_length=254)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='remote_monitoring.machine')),
            ],
        ),
    ]
