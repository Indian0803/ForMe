# Generated by Django 4.0.5 on 2022-07-09 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0012_alter_adviser_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
