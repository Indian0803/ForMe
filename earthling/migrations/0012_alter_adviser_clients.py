# Generated by Django 4.0.5 on 2022-07-07 08:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0011_adviser_clients_alter_adviser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adviser',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
    ]
