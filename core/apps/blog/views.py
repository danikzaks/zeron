from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Category, Post
from .forms import SignUpForm


def index(request):
    return render(request, "blog/index.html")


def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, "blog/category_list.html", {"categories": categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    posts = category.posts.all()
    return render(
        request,
        "blog/category_detail.html",
        {
            "category": category,
            "subcategories": subcategories,
            "posts": posts,
        },
    )


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


def donate(request):
    return render(request, "blog/donate.html")


def success(request):
    return render(request, "success.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('category_list')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('category_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})