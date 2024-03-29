# Generated by Django 2.1.3 on 2018-12-20 04:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20181218_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=2)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['text']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='todo_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todo.ToDo'),
        ),
    ]
