# Generated by Django 4.0.5 on 2022-07-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0013_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('男性', '男性'), ('女性', '女性'), ('その他', 'その他')], max_length=200, null=True),
        ),
    ]
