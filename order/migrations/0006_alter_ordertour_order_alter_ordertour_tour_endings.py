# Generated by Django 4.1.3 on 2022-12-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toursale', '0002_alter_toursale_options_alter_toursale_sale_and_more'),
        ('order', '0005_ordertour_tour_endings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertour',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='ordertour',
            name='tour_endings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='toursale.toursaleend'),
        ),
    ]