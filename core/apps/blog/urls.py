from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
