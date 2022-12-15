from django.db import models


class LandingCurse(models.Model):
    """
    Лэндинг актуальные курсы монеты
    """
    icon = models.ImageField(verbose_name='Логотип', upload_to='media/', db_index=True)
    title = models.CharField(verbose_name='Название банка', db_index=True, max_length=100)
    phone = models.CharField(verbose_name='Номер телефона', db_index=True, max_length=100)

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title


class LandingCurseValue(models.Model):
    """
    Содержимое курсов
    """
    county_choice = (
        (1, 'USD'),
        (2, 'EUR'),
        (3, 'RUB'),
        (4, 'KZT'),
        (5, 'CNY'),
        (6, 'GBP'),
        (7, 'UZS')
    )
    fk = models.ForeignKey(LandingCurse, verbose_name='Банк', on_delete=models.CASCADE)
    buy = models.IntegerField(verbose_name='Покупка', db_index=True)
    shop = models.IntegerField(verbose_name='Продажа', db_index=True)
    county = models.IntegerField(verbose_name='Страна', choices=county_choice, db_index=True)

    class Meta:
        verbose_name = 'Инлайн'
        verbose_name_plural = 'Инлайн'

    def __str__(self):
        return 'Курс'