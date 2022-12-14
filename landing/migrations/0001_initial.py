# Generated by Django 4.1.4 on 2022-12-14 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandingCurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(db_index=True, max_length=100, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='LandingCurseValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.IntegerField(db_index=True, verbose_name='Покупка')),
                ('shop', models.IntegerField(db_index=True, verbose_name='Продажа')),
                ('county', models.IntegerField(choices=[(1, 'USD'), (2, 'EUR'), (3, 'RUB'), (4, 'KZT'), (5, 'CNY'), (6, 'GBP')], db_index=True, verbose_name='Страна')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.landingcurse', verbose_name='Банк')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
