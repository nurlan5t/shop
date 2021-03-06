from django.db import models
from django.db.models import SET_NULL


class Tag(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(verbose_name="Текст", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = "Теги"
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(verbose_name="Текст", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name="Текст", null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=SET_NULL, verbose_name="Категория")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    is_active = models.BooleanField(default=False, verbose_name="В наличии")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')
    def __str__(self):
        return self.title

class ProductImage(models.Model):
    url = models.URLField(null=True)
    product = models.ForeignKey(Product, on_delete=SET_NULL, null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"