# Generated by Django 3.2.7 on 2021-12-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=50, verbose_name='Họ và Tên: ')),
                ('avatar', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(default='', max_length=1000, verbose_name='Mô tả')),
                ('faceBook', models.CharField(default='', max_length=1000, verbose_name='Facebook')),
                ('twitter', models.CharField(default='', max_length=1000, verbose_name='Facebook')),
                ('instagram', models.CharField(default='', max_length=1000, verbose_name='Facebook')),
            ],
            options={
                'db_table': 'about',
            },
        ),
    ]
