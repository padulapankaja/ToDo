# Generated by Django 2.1.3 on 2018-12-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_todo_expdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='expDate',
            field=models.DateField(),
        ),
    ]