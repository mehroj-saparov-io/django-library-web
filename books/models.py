from django.db import models
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    category = models.ManyToManyField(
        Category,
        related_name='books'
    )

    title = models.CharField(max_length=200)
    expert = models.CharField(
        max_length=300,
        help_text="Qisqa tavsif yoki ekspert fikri"
    )

    authors = models.ManyToManyField(
        Author,
        related_name='books'
    )

    description = models.TextField(blank=True)

    created_year = models.PositiveSmallIntegerField(
        help_text="Masalan: 2023"
    )

    image = models.ImageField(
        upload_to='books/images/',
        blank=True,
        null=True
    )

    file = models.FileField(
        upload_to='books/files/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'docx', 'epub']
            )
        ],
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title