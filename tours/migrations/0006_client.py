# Generated by Django 4.1.3 on 2022-11-24 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_alter_tour_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя клиента')),
            ],
        ),
    ]
