# Generated by Django 3.2.16 on 2022-12-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_alter_landingcurse_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingcurse',
            name='value',
            field=models.BooleanField(default=False, verbose_name='Наш банк'),
        ),
        migrations.AlterField(
            model_name='landingcursevalue',
            name='buy',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Покупка'),
        ),
        migrations.AlterField(
            model_name='landingcursevalue',
            name='county',
            field=models.IntegerField(choices=[(1, 'USD'), (2, 'EUR'), (3, 'RUB'), (4, 'KZT'), (5, 'CNY'), (6, 'GBP'), (7, 'UZS')], db_index=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='landingcursevalue',
            name='shop',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Продажа'),
        ),
    ]