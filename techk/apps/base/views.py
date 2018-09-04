# from django.http import HttpResponse
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://books.toscrape.com/').read()
soup = bs.BeautifulSoup(sauce, "html.parser")

#Obtenemos string con categorias desde sitio
categoriesOrigin = soup.find("div", {"class": "side_categories"})
#creamos un array con string de categorias
categorias = categoriesOrigin.ul.li.text.split()
#Eliminamos "Books" del arreglo.
del(categorias[0])

# print(categorias)

booksOrigin = soup.findAll("article", {"class": "product_pod"})
# print(len(booksOrigin))
# print(booksOrigin[1].find("div", {"class": "product_price"}).find("p", {"class": "price_color"}).text)
books = []

class Book():
    title = ""
    price = ""

    def __init__(self, title, price):
        self.title = title
        self.price = price


for i in range(len(booksOrigin)):
    title = booksOrigin[i].h3.a['title']
    price = booksOrigin[i].find("div", {"class": "product_price"}).find("p", {"class": "price_color"}).text
    
    book = Book(title, price)
    # print(book.title)
    books.append(book)
    
for b in books:
    print(b.price)
# print(books[1].price)

# i = 0
# while i < len(booksOrigin)
#     if


# for book in booksOrigin:

# def index(request):
#     return HttpResponse(sopa.title)
