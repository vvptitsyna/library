from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', homeindex, name='home'),
    path('books/', books, name='books'),
]