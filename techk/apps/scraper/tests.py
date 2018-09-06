# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from apps.scraper.models import Category, Book
from .Views import Operation

# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Survival Horror", url="books/survival_horror/")
        Category.objects.create(name="Psychological Thriller", url="books/psychological_thriller/")

    def test_categories_are_saved(self):
        survivalHorror = Category.objects.get(name="Survival Horror")
        psychologicalThriller = Category.objects.get(name="Psychological Thriller")
        self.assertEqual(survivalHorror.url, 'books/survival_horror/')
        self.assertEqual(psychologicalThriller.url, 'books/psychological_thriller/')

# Cabe notar que las pruebas unitarias se usan principalmente para probar metodos creados dentro de un controlador (Views.py, en este caso)...
# Sin embargo para esta aplicacion todos los metodos son para mostrar o insertar datos de una fuente externa.
# Para mostar el funcionamiento de las pruebas de mejor manera, hice una funcion que entreta promedios...

class ConcatStringTestCase(TestCase):
    def test_promedios(self):
        grades = [7, 7, 7, 4, 3, 6, 7, 1]
        prom = Operation.prom(grades)
        exceptedResult = 5.25
        self.assertEqual(prom, exceptedResult)

