# Generated by Django 3.2.7 on 2021-12-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='instagram',
            field=models.CharField(default='', max_length=1000, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='about',
            name='twitter',
            field=models.CharField(default='', max_length=1000, verbose_name='Twiiter'),
        ),
    ]
