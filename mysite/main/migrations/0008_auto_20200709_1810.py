# Generated by Django 3.0.7 on 2020-07-09 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_imp_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imp',
            name='number',
            field=models.IntegerField(default=100),
        ),
    ]
