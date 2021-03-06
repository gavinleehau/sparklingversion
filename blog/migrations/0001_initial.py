# Generated by Django 3.2.7 on 2021-12-25 14:15

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='', max_length=30, verbose_name='Tên tác giảaaa')),
                ('avatar', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='Tiêu đề')),
                ('hashtag', models.CharField(default='', max_length=100, verbose_name='hashtag')),
                ('date', models.DateField(verbose_name='Thời gian đăng')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Nội dung')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
            options={
                'db_table': 'blog',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='decripsion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(default='', max_length=100, verbose_name='Note')),
                ('decripsion', models.TextField(default='', verbose_name='Mô tả')),
            ],
            options={
                'db_table': 'decripsion',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='paragraph_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_paragraph', models.CharField(default='paragraph', max_length=100, verbose_name='Note')),
                ('paragraph', models.TextField(default='', verbose_name='paragraph')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Tên')),
                ('body', models.TextField(verbose_name='Bình luận')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]
