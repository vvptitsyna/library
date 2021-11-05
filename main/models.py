from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default='DEFAULT')
    photo = models.ImageField(upload_to="photos_books/")
    description = models.TextField(default='DEFAULT_DESCRIPTION')
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    genre = models.ManyToManyField('Genre', null=True)

class Author(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default='DEFAULT')
    photo = models.ImageField(upload_to="photos_authors/")
    about_author = models.TextField(default='DEFAULT_DESCRIPTION')

class Genre(models.Model):
    name = models.CharField(max_length=50)
    about_genre = models.TextField(default='DEFAULT_DESCRIPTION')