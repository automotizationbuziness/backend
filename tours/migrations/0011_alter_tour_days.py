# Generated by Django 4.1.3 on 2022-11-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_tour_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='days',
            field=models.IntegerField(null=True),
        ),
    ]
