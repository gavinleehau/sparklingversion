# Generated by Django 3.2.7 on 2021-12-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20211225_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='', max_length=100, verbose_name='Vị trí ')),
                ('phone', models.CharField(default='', max_length=15, verbose_name='Số điện thoại ')),
                ('email_footer', models.CharField(default='', max_length=100, verbose_name='Email ')),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='email_footer',
        ),
        migrations.RemoveField(
            model_name='about',
            name='location',
        ),
        migrations.RemoveField(
            model_name='about',
            name='phone',
        ),
    ]
