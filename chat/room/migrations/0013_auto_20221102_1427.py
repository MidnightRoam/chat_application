# Generated by Django 3.2 on 2022-11-02 13:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0012_auto_20221102_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 11, 2, 13, 27, 33, 388753, tzinfo=utc)),
        ),
    ]
