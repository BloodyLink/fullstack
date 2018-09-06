# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.TextField()
    url = models.TextField()
    price = models.TextField()
    stock = models.IntegerField();
    description = models.TextField()
    upc = models.CharField(max_length=50)
    def __str__(self):
        return self.title