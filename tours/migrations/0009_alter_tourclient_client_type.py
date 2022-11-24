# Generated by Django 4.1.3 on 2022-11-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0008_alter_tourclient_options_alter_tourclient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourclient',
            name='client_type',
            field=models.CharField(choices=[('Физическое лицо', 'Физическое лицо'), ('Юридическое лицо', 'Юридическое лицо')], default=('Физическое лицо', 'Физическое лицо'), max_length=100, verbose_name='Тип клиента'),
        ),
    ]
