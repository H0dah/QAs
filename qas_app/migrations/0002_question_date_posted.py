# Generated by Django 3.0.7 on 2020-08-26 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
 