from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="subcategories",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    def get_full_path(self):
        categories = []
        category = self
        while category:
            categories.append(category.name)
            category = category.parent
        return " > ".join(reversed(categories))


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
