# Generated by Django 4.1.4 on 2022-12-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='landingcurse',
            options={'verbose_name': 'Курсы', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='landingcursevalue',
            options={'verbose_name': 'Инлайн', 'verbose_name_plural': 'Инлайн'},
        ),
        migrations.AddField(
            model_name='landingcurse',
            name='icon',
            field=models.ImageField(db_index=True, default=1, upload_to='media/', verbose_name='Логотип'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landingcurse',
            name='title',
            field=models.CharField(db_index=True, default=1, max_length=100, verbose_name='Название банка'),
            preserve_default=False,
        ),
    ]
