import random

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

def homeindex(request):
    books = Book.objects.all()
    book_random = get_random_book()
    return render(request, 'main/main.html', {'books': books, 'book_random': book_random})
# Create your views here.
