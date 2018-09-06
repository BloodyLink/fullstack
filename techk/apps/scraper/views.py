# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from apps.scraper.models import Category, Book
from django.http import HttpResponse
import bs4 as bs
import urllib.request

#Obtenemos todas las categorias y sus links correspondientes.
def getAllCategories():
    print("Getting All Categories...")
    sauce = urllib.request.urlopen('http://books.toscrape.com/').read()
    soup = bs.BeautifulSoup(sauce, "html.parser")
    #Obtenemos string con categorias desde sitio
    categoriesOrigin = soup.find("div", {"class": "side_categories"})
    #creamos un array con string de categorias
    for cat in categoriesOrigin.ul.li.ul.find_all('a'):
        catUrl = cat.get('href')
        catName = cat.text.strip()
        Category.objects.get_or_create(name=catName, url=catUrl)


#ahora guardaremos los libros por categoria.
def getAllBooks():
    print("Getting All Books...")
    for cat in Category.objects.all():
        for i in range(1, 20):
            page = cat.url.replace('index.html', 'page-')
            try:
                salsa = urllib.request.urlopen('http://books.toscrape.com/' + page + '%s.html' % i).read()
            except urllib.error.HTTPError:
                break
            sopa = bs.BeautifulSoup(salsa, "html.parser")
            booksOrigin = sopa.findAll("article", {"class": "product_pod"})
            books = []

            for i in range(len(booksOrigin)):
                category = cat.id
                title = booksOrigin[i].h3.a['title']
                price = booksOrigin[i].find("div", {"class": "product_price"}).find("p", {"class": "price_color"}).text
                thumbnail = booksOrigin[i].find("div", {"class": "image_container"}).find("img", {"class", "thumbnail"}).get('src')
                thumbnail = thumbnail.replace('../../../..', '')
                url = booksOrigin[i].find("div", {"class": "image_container"}).find("a").get("href")
                url = url.replace('../../..', 'catalogue')
                # print(thumbnail)
                stock = 1
                Book.objects.get_or_create(category_id=category, title=title, price=price, thumbnail=thumbnail, url=url, stock="0", description=" ", upc=" ")

            
#Por ultimo... los detalles faltantes de cada libro...
def getBooksDetails():
    print("Getting Book Details...")
    for lib in Book.objects.all():
        # print('http://books.toscrape.com/' + lib.url)
        try:
            salsa = urllib.request.urlopen('http://books.toscrape.com/' + lib.url).read()
        except urllib.error.HTTPError:
            break
        sopa = bs.BeautifulSoup(salsa, "html.parser")
        description = sopa.find("p", {"class": None}).string
        description = description.replace('...more', '')
        stock = sopa.find("p", {"class": "availability"}).text
        stock = int(''.join(filter(str.isdigit, stock)))
        upc = sopa.find("table", {"class", "table-striped"}).tr.td.text
        lib.description = description
        lib.stock = stock
        lib.upc = upc
        lib.save()




def index(request):
    return HttpResponse(links)


# cat = Category.objects.all()

# print(cat)

# booksOrigin = soup.findAll("article", {"class": "product_pod"})
# # print(len(booksOrigin))
# # print(booksOrigin[1].find("div", {"class": "product_price"}).find("p", {"class": "price_color"}).text)
# books = []

# class Book():
#     title = ""
#     price = ""

#     def __init__(self, title, price):
#         self.title = title
#         self.price = price


# for i in range(len(booksOrigin)):
#     title = booksOrigin[i].h3.a['title']
#     price = booksOrigin[i].find("div", {"class": "product_price"}).find("p", {"class": "price_color"}).text
    
#     book = Book(title, price)
#     # print(book.title)
#     books.append(book)
    
# for b in books:
#     print(b.price)
# print(books[1].price)

# i = 0
# while i < len(booksOrigin)
#     if


# for book in booksOrigin:


