# Generated by Django 4.0.5 on 2022-07-15 07:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('earthling', '0023_alter_thread_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 15, 16, 53, 19, 352926)),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='レビューコメント')),
                ('score', models.PositiveSmallIntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default='3', verbose_name='レビュースコア')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
