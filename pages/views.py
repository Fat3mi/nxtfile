from django.shortcuts import render
from .models import Book,category
from django.views import generic
from django.db.models import Q
# Create your views here.

def home(request):
    last_books=Book.objects.all()[:4]
    return render(request,'pages/home.html',context={'last_books':last_books})

class BookListView(generic.ListView):
    model = Book
    paginate_by=16
    template_name = "pages/list.html"
    context_object_name='books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "pages/detail.html"
    context_object_name='book'

class search_book(generic.ListView):
    template_name='pages/list.html'
    paginate_by=16
    model=Book
    context_object_name='books'
    # paginate_by=9
    def get_queryset(self):
        query=self.request.GET.get("search")
        books = Book.objects.all().filter(Q(title__icontains=query) | Q(description__icontains=query)) 
        return books