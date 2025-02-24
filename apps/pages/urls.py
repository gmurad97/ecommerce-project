from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.home),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("faq/", views.faq, name="faq"),
    path("gallery/", views.gallery, name="gallery"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<slug:slug_id>", views.category_products, name="category_products"),
    path("products/", views.product_list, name="product_list"),
    path("products/<slug:slug_id>", views.product_detail, name="product_detail"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
]
