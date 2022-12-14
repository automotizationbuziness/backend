# Generated by Django 4.1.3 on 2022-11-14 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя администратора')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия администратора')),
                ('midname', models.CharField(max_length=200, verbose_name='Отчество администратора')),
            ],
            options={
                'verbose_name': 'Администратор отеля',
                'verbose_name_plural': 'Администраторы отелей',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название места')),
            ],
            options={
                'verbose_name': 'Местонахождение',
                'verbose_name_plural': 'Местонахождения',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название отеля')),
                ('phone', models.CharField(max_length=100, verbose_name='Контактный телефон')),
                ('description', models.TextField(verbose_name='Описание отеля')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hoteladmin', verbose_name='Администратор отеля')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.place', verbose_name='Местонахождение отеля')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
    ]
