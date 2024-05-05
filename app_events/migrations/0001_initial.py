# Generated by Django 4.0.1 on 2024-05-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('datetime', models.DateTimeField(verbose_name='Дата')),
                ('datetime_event', models.DateTimeField(verbose_name='Дата Ивента')),
                ('image', models.ImageField(upload_to='event_images/', verbose_name='Изображение')),
                ('extended_image', models.ImageField(upload_to='extended_event_images/', verbose_name='Иконка')),
                ('duration', models.CharField(max_length=255, verbose_name='Продолжительность')),
                ('speaker_name', models.CharField(max_length=255, verbose_name='Спикер')),
                ('free_spots', models.IntegerField(verbose_name='Свободные места')),
            ],
            options={
                'verbose_name': 'Ивент',
                'verbose_name_plural': 'Ивенты',
            },
        ),
        migrations.AddIndex(
            model_name='events',
            index=models.Index(fields=['id'], name='app_events__id_719de4_idx'),
        ),
        migrations.AddIndex(
            model_name='events',
            index=models.Index(fields=['title'], name='app_events__title_d19fb7_idx'),
        ),
    ]