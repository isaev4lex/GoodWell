from django.db import models


class MainBanner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', blank=False)
    subtitle = models.CharField(max_length=200, verbose_name='Подзаголовок', blank=True)
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок (УЗБ)', blank=False)
    subtitle_uz = models.CharField(max_length=200, verbose_name='Подзаголовок (УЗБ)', blank=True)
    img = models.ImageField(upload_to='media', verbose_name='Баннер', blank=False)
    link = models.TextField(verbose_name='Ссылка на страницу')

    class Meta:
        verbose_name = 'Главный баннер'
        verbose_name_plural = 'Главные баннеры'

    def __str__(self):
        return self.title


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Title (УЗБ)', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title
