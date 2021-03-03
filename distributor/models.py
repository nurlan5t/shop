from django.db import models
from django.db.models import SET_NULL


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=SET_NULL)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title