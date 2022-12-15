# Generated by Django 4.1.3 on 2022-12-15 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0015_tour_created'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='payed_sum',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=100, null=True, verbose_name='Остаток на счете'),
        ),
        migrations.AlterField(
            model_name='reporttable',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tour', verbose_name='Тур'),
        ),
    ]