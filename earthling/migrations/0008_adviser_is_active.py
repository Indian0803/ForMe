# Generated by Django 4.0.5 on 2022-07-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0007_alter_adviser_facebook_alter_adviser_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adviser',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]