from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', homeindex.as_view(), name='home'),
    path('books/', books.as_view(), name='books'),
    path('authors/', authors.as_view(), name='authors'),
    path('genres/', genres.as_view(), name='genres'),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name='show_book'),
    path('author/<slug:author_slug>/', ShowAuthor.as_view(), name='show_author'),
    path('genre/<slug:genre_slug>/', ShowGenre.as_view(), name='show_genre'),
]