# Generated by Django 3.0.8 on 2020-07-13 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200713_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readinglist',
            name='description',
        ),
    ]