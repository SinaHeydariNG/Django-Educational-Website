# Generated by Django 4.1.1 on 2022-10-07 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_usercourses_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourses',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 8, 16, 17, 508883)),
        ),
    ]
