# Generated by Django 2.1.3 on 2018-12-29 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20181229_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='cuDate',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
