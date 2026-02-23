from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Category, Author
from django.db.models import Q


def home(request):
    # Base queryset
    queryset = Book.objects.prefetch_related('category', 'authors')

    # Category filter
    category_id = request.GET.get('category')
    if category_id:
        queryset = queryset.filter(category__id=category_id)

    # Search
    q = request.GET.get('q', '').strip()
    if q:
        queryset = queryset.filter(
            Q(title__icontains=q) |
            Q(expert__icontains=q) |
            Q(authors__full_name__icontains=q) |
            Q(category__name__icontains=q)
        ).distinct()

    context = {
        'books': queryset.distinct(),
        'categories': Category.objects.all(),
        'query': q,
        'selected_category': category_id
    }
    return render(request, 'home.html', context)


def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.prefetch_related('category', 'authors'),
        pk=pk
    )
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)