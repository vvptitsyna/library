from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название книги")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    year = models.IntegerField(verbose_name="Год выпуска")
    photo = models.ImageField(upload_to="photos_books/", verbose_name="Фотография")
    description = models.TextField(verbose_name="Описание")
    author = models.ForeignKey('Author', on_delete=models.PROTECT, verbose_name="Автор книги")
    genre = models.ManyToManyField('Genre', verbose_name="Жанр")

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="ФИО автора")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    year = models.CharField(max_length=9, verbose_name="Года жизни")
    photo = models.ImageField(upload_to="photos_authors/", verbose_name="Фотография")
    about_author = models.TextField(verbose_name="Об авторе")

class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название жанра")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    about_genre = models.TextField(verbose_name="О жанре")