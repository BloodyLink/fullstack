from django.http import HttpResponse
from django.template import loader
from apps.scraper.models import Category, Book

def index(request):
    # return HttpResponse(links)
    categories = Category.objects.all()
    template = loader.get_template('base/index.html')
    context = {
        'categories': categories
    }
    return HttpResponse(template.render(context, request))

def books(request):

    id = request.GET.get('cat_id')

    if(id == 'none'):
        bookList = Book.objects.all()
    else:
        id = request.GET.get('cat_id')
        bookList = Book.objects.filter(category_id=id).all()
    
    template = loader.get_template('base/books.html')
    context = {
        'books': bookList
    }
    return HttpResponse(template.render(context, request))