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
    categories = Category.objects.all()
    if(id == 'none'):
        bookList = Book.objects.all()
    else:
        bookList = Book.objects.filter(category_id=id).all()
    
    template = loader.get_template('base/books.html')
    context = {
        'books': bookList
        'categories': categories
    }
    return HttpResponse(template.render(context, request))

def bookDetails(request):
    id = request.GET.get('book_id')

    if(id == 'none'):
        return HttpResponse("No existe libro con id " + id)
    else:
        bookDetails = Book.objects.get(id=id)
    
    template = loader.get_template('base/book_details.html')
    context = {
        'book': bookDetails
    }
    return HttpResponse(template.render(context, request)) 

def bookDelete(request):
    id = request.GET.get('book_id')

    if(id == 'none'):
        return HttpResponse("No existe libro con id " + id)
    else:
        bookDetails = Book.objects.get(id=id)
        bookDetails.delete()
        return HttpResponse("Libro con id " + id + " eliminado.")

def bookSearch(request):
    word = request.POST.get('word')
    categories = Category.objects.all()
    books = Book.objects.filter(string__icontains=word)
    template = loader.get_template('base/books.html')
    context = {
        'books': books
        'categories': categories
    }
    return HttpResponse(template.render(context, request))