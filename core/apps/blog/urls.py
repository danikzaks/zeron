from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.category_list, name="category_list"),
    path("category/<int:category_id>/", views.category_detail, name="category_detail"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("donate/", views.donate, name="donate"),
    path("success/", views.success, name="success"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
]
