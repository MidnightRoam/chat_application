# Generated by Django 3.2 on 2022-10-31 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 15, 9, 0, 303286, tzinfo=utc)),
        ),
    ]