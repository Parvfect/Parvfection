# Generated by Django 3.0.7 on 2020-07-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_imp_projects_readinglist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imp',
            options={'verbose_name_plural': 'Impossible List'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='readinglist',
            options={'verbose_name_plural': 'Reading List'},
        ),
        migrations.RemoveField(
            model_name='imp',
            name='date',
        ),
        migrations.RemoveField(
            model_name='imp',
            name='status',
        ),
        migrations.AlterField(
            model_name='imp',
            name='sub',
            field=models.TextField(),
        ),
    ]
