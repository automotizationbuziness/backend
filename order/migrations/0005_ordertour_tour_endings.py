# Generated by Django 4.1.3 on 2022-12-06 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toursale', '0002_alter_toursale_options_alter_toursale_sale_and_more'),
        ('order', '0004_remove_order_total_cost_alter_ordertour_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertour',
            name='tour_endings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='toursale.toursaleend'),
        ),
    ]
