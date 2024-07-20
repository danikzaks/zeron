from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def index(request):
    return render(request, "blog/index.html")


def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, 'blog/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    posts = category.posts.all()
    return render(request, 'blog/category_detail.html', {
        'category': category,
        'subcategories': subcategories,
        'posts': posts,
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def donate(request):
    return render(request, 'blog/donate.html')

def success(request):
    return render(request, 'success.html')
