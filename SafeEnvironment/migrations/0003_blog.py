# Generated by Django 3.0.3 on 2020-03-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environmentApp', '0002_auto_20200330_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogID', models.CharField(max_length=250, unique=True)),
                ('sucject', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
