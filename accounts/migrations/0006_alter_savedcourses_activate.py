# Generated by Django 4.1.1 on 2022-10-13 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_savedcourses_activate_alter_savedcourses_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcourses',
            name='activate',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 13, 40, 9, 890672)),
        ),
    ]
