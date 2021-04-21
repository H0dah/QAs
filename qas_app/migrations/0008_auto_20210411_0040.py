# Generated by Django 3.0.7 on 2021-04-10 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qas_app', '0007_auto_20210325_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date_answered',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
