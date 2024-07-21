from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from .models import Category, Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ["title", "content", "category"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "get_full_path")


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    form = PostAdminForm


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
