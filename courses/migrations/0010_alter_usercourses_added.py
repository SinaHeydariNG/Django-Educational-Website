# Generated by Django 4.1.1 on 2022-10-07 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_usercourses_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourses',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 8, 43, 43, 360067)),
        ),
    ]
