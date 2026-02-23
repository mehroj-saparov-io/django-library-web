from django.urls import path
from .views import home, book_detail

app_name = 'books'

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
]