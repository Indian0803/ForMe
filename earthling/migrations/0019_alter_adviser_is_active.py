# Generated by Django 4.0.5 on 2022-07-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0018_alter_adviser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adviser',
            name='is_active',
            field=models.BooleanField(choices=[(True, '依頼を受け付ける'), (False, '依頼募集を停止する')], default=False, null=True),
        ),
    ]
