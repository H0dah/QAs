# Generated by Django 3.0.7 on 2021-03-25 14:22

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qas_app', '0005_auto_20200830_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asked_user',
            field=models.CharField(default=1, max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
    ]