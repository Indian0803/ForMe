# Generated by Django 4.0.5 on 2022-07-15 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0021_chatmessage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
