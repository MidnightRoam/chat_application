# Generated by Django 3.2 on 2022-10-31 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_room_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 15, 10, 42, 798038, tzinfo=utc)),
        ),
    ]
