# Generated by Django 4.1.3 on 2022-12-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_ordertour_tour_endings'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('Завершен (положительно)', 'Завершен (положительно)'), ('Действует', 'Действует'), ('Отменен', 'Отменен')], default='Действует', max_length=100),
        ),
    ]
