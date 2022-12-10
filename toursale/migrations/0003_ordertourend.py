# Generated by Django 4.1.3 on 2022-12-10 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0014_alter_tour_days_alter_tour_nights'),
        ('toursale', '0002_alter_toursale_options_alter_toursale_sale_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTourEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=100, max_length=100, verbose_name='Цена (руб.)')),
                ('tourist_amount', models.PositiveIntegerField(verbose_name='Количество человек')),
                ('total_cost', models.DecimalField(decimal_places=2, editable=False, max_digits=100, max_length=100, verbose_name='Стоимость (руб.)')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tour', verbose_name='Тур')),
                ('tour_endings', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='toursale.toursaleend')),
            ],
            options={
                'verbose_name': 'Продаваемый тур',
                'verbose_name_plural': 'Список продаваемых туров',
            },
        ),
    ]