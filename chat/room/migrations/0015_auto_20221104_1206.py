# Generated by Django 3.2 on 2022-11-04 11:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0014_auto_20221104_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 11, 4, 11, 6, 53, 137214, tzinfo=utc)),
        ),
    ]