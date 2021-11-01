from django.db import models


class Partners(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Логотип', blank=False)

    class Meta:
        verbose_name = 'Партнёра'
        verbose_name_plural = 'Партнёры'

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
