# Generated by Django 3.2 on 2022-11-01 15:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_auto_20221101_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 15, 7, 51, 504201, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 11, 1, 15, 7, 51, 503200, tzinfo=utc)),
        ),
    ]
