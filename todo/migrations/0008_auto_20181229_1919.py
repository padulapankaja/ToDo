# Generated by Django 2.1.3 on 2018-12-29 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20181229_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='expDate',
            field=models.DateField(default=datetime.date.today, verbose_name=()),
        ),
    ]