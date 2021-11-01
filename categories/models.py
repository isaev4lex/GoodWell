from django.db import models
from django.urls import reverse
from .ru_to_eng import translate


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', blank=False)
    title_uz = models.CharField(max_length=150, verbose_name='Название (УЗБ)', blank=False)
    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('categories', args=[self.slug])

    def get_url_uz(self):
        return reverse('categories', args=[self.slug, 'uz'])


class Paint(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Название (УЗБ)', blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paint_temp_from = models.CharField(max_length=10, verbose_name='Температура применения краски ОТ', blank=True)
    paint_temp_to = models.CharField(max_length=10, verbose_name='Температура применения краски ДО', blank=True)
    usage_temp_from = models.CharField(max_length=10, verbose_name='Температура эксплуатации покрытия ОТ', blank=True)
    usage_temp_to = models.CharField(max_length=10, verbose_name='Температура эксплуатации покрытия ДО', blank=True)
    service_life = models.CharField(max_length=10, verbose_name='Срок эксплуатации не менее скольки лет?', blank=True)
    packaging = models.CharField(max_length=40, verbose_name='Об упаковке', blank=True)
    color = models.CharField(max_length=100, verbose_name='Цвет', blank=True)
    made_in = models.CharField(max_length=100, verbose_name='Страна производителя', blank=True)
    color_uz = models.CharField(max_length=100, verbose_name='Цвет (УЗБ)', blank=True)
    made_in_uz = models.CharField(max_length=100, verbose_name='Страна производителя (УЗБ)', blank=True)

    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)
    price = models.CharField(max_length=100, verbose_name='Цена', blank=False)

    usage_description = models.TextField(verbose_name='Особенности применения и эксплуатации', blank=False)
    usage_description_uz = models.TextField(verbose_name='Особенности применения и эксплуатаци (УЗБ)', blank=False)
    how_to_save_description = models.TextField(verbose_name='Условия транспортирования и хранения', blank=True)
    how_to_save_description_uz = models.TextField(verbose_name='Условия транспортирования и хранения (УЗБ)', blank=True)
    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)

    class Meta:
        verbose_name = 'Краску'
        verbose_name_plural = 'Краски'

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('product', args=[self.slug])

    def get_url_uz(self):
        return reverse('product', args=[self.slug, 'uz'])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)


class TechnicInfo(models.Model):
    for_product_info = models.ForeignKey(Paint, on_delete=models.CASCADE, verbose_name='Для продукта', default=None)
    fire_resistant_efficiency_group = models.CharField(max_length=3, verbose_name='Какая группа огнезащитной эффективности', blank=True)
    fire_resistant_efficiency_min = models.CharField(max_length=3, verbose_name='Сколько минут?', blank=True)
    reduced_thickness = models.CharField(max_length=5, verbose_name='Приведенная толщина металла, мм', blank=True)
    dry_thickness_paint_layer = models.CharField(max_length=8, verbose_name='Толщина сухого слоя краски, мм', blank=True)
    consumption_paint = models.CharField(max_length=8, verbose_name='Теоретический расход краски, кг/м', blank=True)


class FlameRetard(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Название (УЗБ)', blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_group = models.CharField(max_length=10, verbose_name='Первая группа огнезащитной эффективности. Расход не менее скольки литров (мл/м)?', blank=True)
    second_group = models.CharField(max_length=10, verbose_name='Вторая группа огнезащитной эффективности. Расход не менее скольки литров (мл\м)?', blank=True)
    temp_usage_from = models.CharField(max_length=8, verbose_name='Температура использования ОТ', blank=False)
    temp_usage_to = models.CharField(max_length=8, verbose_name='Температура использования ДО', blank=False)
    usage_without_lost = models.CharField(max_length=20, verbose_name='Расход без учёта потерь (МЛ)', blank=True)
    packaging = models.CharField(max_length=40, verbose_name='Об упаковке', blank=False)
    ready_time = models.CharField(max_length=2, verbose_name='Сколько часов сохнет?', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)
    price = models.CharField(max_length=100, verbose_name='Цена', blank=False)
    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)

    class Meta:
        verbose_name = 'Огнезащитную смесь'
        verbose_name_plural = 'Огнезащитные смеси'

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('product', args=[self.slug])

    def get_url_uz(self):
        return reverse('product', args=[self.slug, 'uz'])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)


class Tubes(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Название (УЗБ)', blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)
    price = models.CharField(max_length=100, verbose_name='Цена', blank=True, default='')
    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)

    class Meta:
        verbose_name = 'Трубу'
        verbose_name_plural = 'Трубы'

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('product', args=[self.slug])

    def get_url_uz(self):
        return reverse('product', args=[self.slug, 'uz'])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)


class TechnicTubesInfo(models.Model):
    for_product_info = models.ForeignKey(Tubes, on_delete=models.CASCADE, verbose_name='Для продукта')
    naming = models.CharField(max_length=20, verbose_name='Наименование', blank=True)
    diameter = models.CharField(max_length=10, verbose_name='Диаметр (мм)', blank=True)
    square = models.CharField(max_length=10, verbose_name='Площадь (мм)', blank=True)
    weight = models.CharField(max_length=10, verbose_name='Вес (кг)', blank=True)

    class Meta:
        verbose_name = 'Тех Информация'
        verbose_name_plural = 'Тех Информация'


class Fitting(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Название (УЗБ)', blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)
    # price = models.CharField(max_length=100, verbose_name='Цена', blank=False)
    # slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)

    class Meta:
        verbose_name = 'Фитинг'
        verbose_name_plural = 'Фитинги'

    def __str__(self):
        return self.title
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = translate(self.title)
    #     super().save(*args, **kwargs)


class Alarm(models.Model):
    title = models.CharField(max_length=120, verbose_name='Название', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Название (УЗБ)', blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)
    # price = models.CharField(max_length=100, verbose_name='Цена', blank=False)
    # slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.title
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = translate(self.title)
    #     super().save(*args, **kwargs)


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
