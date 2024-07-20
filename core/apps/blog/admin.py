from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "get_full_path")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
