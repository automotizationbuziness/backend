# Generated by Django 4.1.3 on 2022-11-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_tour_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=32, verbose_name='Цена тура (руб.)'),
        ),
    ]
