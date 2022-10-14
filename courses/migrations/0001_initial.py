# Generated by Django 4.1.1 on 2022-10-01 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.ImageField(upload_to='courses/%y/%m/%d')),
                ('information', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category')),
            ],
        ),
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('thumbnail', models.ImageField(upload_to='episodes/%y/%m/%d')),
                ('information', models.TextField()),
                ('status', models.CharField(choices=[('AVAILABEL', 'AVAILABEL'), ('LOCKED', 'LOCKED')], default='AVAILABEL', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='courses.courses')),
            ],
        ),
    ]