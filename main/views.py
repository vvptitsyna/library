import random

from django.views.generic import ListView, DetailView
from django.db.models import Max
from django.shortcuts import render

from .models import *

def get_random_book():
        max_id = Book.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            book_random = Book.objects.filter(pk=pk).first()
            if book_random:
                return book_random



class homeindex(ListView):
    model = Book
    template_name = 'main/main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_random'] = get_random_book()
        return context


class books(ListView):
    paginate_by = 9
    model = Book
    template_name = 'main/books.html'
    context_object_name = 'collection_books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class authors(ListView):
    paginate_by = 2
    model = Author
    template_name = 'main/authors.html'
    context_object_name = 'authors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class genres(ListView):
    paginate_by = 9
    model = Genre
    template_name = 'main/genres.html'
    context_object_name = 'genres'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ShowBook(DetailView):
    model = Book
    template_name = 'main/book.html'
    slug_url_kwarg = 'book_slug'
    context_object_name = 'book'

class ShowAuthor(DetailView):
    model = Author
    template_name = 'main/author.html'
    slug_url_kwarg = 'author_slug'
    context_object_name = 'author'

class ShowGenre(DetailView):
    model = Genre
    template_name = 'main/genre.html'
    slug_url_kwarg = 'genre_slug'
    context_object_name = 'genre'
