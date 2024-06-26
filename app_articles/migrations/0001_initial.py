# Generated by Django 4.0.1 on 2024-05-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='articles/%Y/%m/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Изображение Новостей',
                'verbose_name_plural': 'Изображения Новостей',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Загаловка')),
                ('short_description', models.TextField(verbose_name='Краткое Описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_created', models.DateField(verbose_name='Дата создание')),
                ('images', models.ManyToManyField(to='app_articles.ImageArticles', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
