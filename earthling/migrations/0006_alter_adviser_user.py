# Generated by Django 4.0.5 on 2022-07-01 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0005_adviser_count_adviser_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adviser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
