from django.db import models


class Favicon(models.Model):
    favicon = models.ImageField(upload_to='media', verbose_name='Favicon', blank=True)

    class Meta:
        verbose_name = 'Favicon'
        verbose_name_plural = 'Favicon'

    def __str__(self):
        return 'Иконка сайта'


class HeadTags(models.Model):
    title = models.CharField(max_length=100, verbose_name='Для чего этот тэг?', blank=False)
    tag = models.TextField(verbose_name='HTML-Код, для <head> элемента', blank=True)

    class Meta:
        verbose_name = 'Тэг для <head>'
        verbose_name_plural = 'Тэги для <head>'

    def __str__(self):
        return self.title
