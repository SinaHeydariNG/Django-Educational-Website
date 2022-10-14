# Generated by Django 4.1.1 on 2022-10-07 15:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', ckeditor.fields.RichTextField()),
                ('location', models.CharField(default=1, max_length=225)),
                ('phone', models.CharField(default=1, max_length=225)),
                ('logo', models.ImageField(upload_to='logo/%y/%m/%d/')),
                ('email', models.EmailField(default='imsinacoder@gamil.com', max_length=254)),
                ('copyright', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Informations',
            },
        ),
    ]
