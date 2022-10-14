# Generated by Django 4.1.1 on 2022-10-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('url', models.URLField()),
                ('img', models.ImageField(upload_to='socials/%y/%m/%d')),
            ],
        ),
    ]
