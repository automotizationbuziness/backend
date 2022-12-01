# Generated by Django 4.1.3 on 2022-12-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options_alter_order_client_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordertour',
            options={'verbose_name': 'Продаваемый тур', 'verbose_name_plural': 'Список продаваемых туров'},
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=100, verbose_name='Общая стоимость заказа'),
        ),
    ]