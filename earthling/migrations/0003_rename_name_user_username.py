# Generated by Django 4.0.5 on 2022-06-30 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0002_user_gender_alter_user_birth_alter_user_is_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
