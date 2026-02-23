from django.contrib import admin
from .models import Category, Author, Book
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)
    ordering = ('full_name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_year',
        'created_at',
        'is_file_uploaded',
        'image_preview',
    )

    list_filter = (
        'created_year',
        'created_at',
        'category',
        'authors',
    )

    search_fields = (
        'title',
        'expert',
        'description',
        'authors__full_name',
        'category__name',
    )

    ordering = ('-created_at',)

    filter_horizontal = (
        'category',
        'authors',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'image_preview',
    )

    fieldsets = (
        ('Asosiy maʼlumotlar', {
            'fields': (
                'title',
                'expert',
                'description',
                'created_year',
            )
        }),
        ('Bog‘lanishlar', {
            'fields': (
                'category',
                'authors',
            )
        }),
        ('Media', {
            'fields': (
                'image',
                'image_preview',
                'file',
            )
        }),
        ('Vaqtlar', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height: 60px; border-radius: 4px;" />',
                obj.image.url
            )
        return "—"

    image_preview.short_description = "Rasm"

    def is_file_uploaded(self, obj):
        return bool(obj.file)

    is_file_uploaded.boolean = True
    is_file_uploaded.short_description = "Fayl bormi?"