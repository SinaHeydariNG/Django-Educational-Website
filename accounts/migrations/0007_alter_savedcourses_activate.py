# Generated by Django 4.1.2 on 2022-10-14 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_savedcourses_activate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcourses',
            name='activate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 14, 9, 2, 49, 904928)),
        ),
    ]
