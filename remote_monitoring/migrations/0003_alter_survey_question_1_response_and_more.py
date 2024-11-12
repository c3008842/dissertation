# Generated by Django 5.1.1 on 2024-11-04 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_monitoring', '0002_remove_session_remote_moni_machine_603119_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='question_1_response',
            field=models.BooleanField(default='N/A', null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='question_2_response',
            field=models.BooleanField(default='N/A', null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='usermetrics',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='remote_monitoring.usermetrics'),
        ),
    ]
