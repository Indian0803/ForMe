# Generated by Django 4.0.5 on 2022-07-18 06:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0026_user_bone_user_color_alter_thread_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bone',
            new_name='bone_type',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='color',
            new_name='color_type',
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thread',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 18, 15, 18, 18, 92511)),
        ),
        migrations.CreateModel(
            name='ColorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('two', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('three', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('four', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('five', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('six', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('seven', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('eight', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('nine', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('ten', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('eleven', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C'), ('3', 'D')], null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BoneType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('two', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('three', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('four', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('five', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('six', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('seven', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('eight', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('nine', models.PositiveSmallIntegerField(choices=[('0', 'A'), ('1', 'B'), ('2', 'C')], null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bone', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
