# Generated by Django 5.0.3 on 2024-04-07 04:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 8, 4, 52, 52, 951326, tzinfo=datetime.timezone.utc)),
        ),
    ]