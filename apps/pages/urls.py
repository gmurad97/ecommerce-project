from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="index"),

    path("products/", views.index, name="product_list"),
    path("products/<slug:slug_id>/", views.index, name="product_detail"),
    path("categories/", views.index, name="category_list"),
    path("categories/<slug:slug_id>/", views.index, name="category_products"),


    path("contacts/", views.index, name="index"),
    path("about/", views.index, name="index"),
    path("gallery/", views.index, name="index"),
    path("login/", views.index, name="index"),
    path("register/", views.index, name="index"),
    
    path("news/", views.index, name="index"),
    path("news/<slug:slug_id>", views.index, name="index"),
]
