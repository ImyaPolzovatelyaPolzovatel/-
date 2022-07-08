# Generated by Django 4.0.5 on 2022-07-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.CharField(max_length=20, verbose_name='Краткое описание')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagesNews', verbose_name='Изображение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата новости')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('show_on_manepage', models.BooleanField(default=False, verbose_name='Показывать на главной странице')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
