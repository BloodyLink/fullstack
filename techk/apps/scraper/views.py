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
    #guardamos cada una en la BD
    for cat in categoriesOrigin.ul.li.ul.find_all('a'):
        catUrl = cat.get('href')
        catName = cat.text.strip()
        Category.objects.get_or_create(name=catName, url=catUrl)
    
    return "ok"

#Guardaremos los libros por categoria.
def getAllBooks():
    print("Getting All Books...")
    for cat in Category.objects.all():
        for i in range(1, 300):
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

                #Ahora obtendremos los detalles de este libro...
                salsa = urllib.request.urlopen('http://books.toscrape.com/' + url).read()
                sopa = bs.BeautifulSoup(salsa, "html.parser")
                description = sopa.find("p", {"class": None}).string
                description = description.replace('...more', '')
                stock = sopa.find("p", {"class": "availability"}).text
                stock = int(''.join(filter(str.isdigit, stock)))
                upc = sopa.find("table", {"class", "table-striped"}).tr.td.text

                #Y guardamos todo...
                Book.objects.get_or_create(category_id=category, title=title, price=price, thumbnail=thumbnail, url=url, stock=stock, description=description, upc=upc)
    return "ok"

def updateDatabase(){

    try:
        getAllCategories()
        getAllBooks()
    except NameError:
        print("There was an error trying to update the database.")

    return HttpResponse("Database Updated.")
}
class Operation(){
    def prom(grades):
        sum = 0;
        for grade in grades:
            sum += grade
        prom = sum / len(grades)
        return prom
}

