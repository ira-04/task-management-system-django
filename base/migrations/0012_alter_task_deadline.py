# Generated by Django 5.0.3 on 2024-04-06 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_task_deadline_alter_task_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 7, 14, 46, 25, 287015, tzinfo=datetime.timezone.utc)),
        ),
    ]