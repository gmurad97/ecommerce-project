from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),

#==============================dynamic
    # brands - home
    # brands/adidas - products this brand
    path("brands/", views.brand_list, name="brand_list"),
    path("brands/<slug:slug_id>", views.brand_products, name="brand_products"),

    # categories - home
    # categories/shoes - products this category
    path("categories/", views.category_list, name="category_list"),
    path("categories/<slug:slug_id>", views.category_products, name="category_products"),

    # brands - home
    # brands/adidas - products this brand
    path("products/", views.product_list, name="product_list"),
    path("products/<slug:slug_id>", views.product_detail, name="product_detail"),
#==============================end



    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("about/", views.about, name="about"),


    path("auth/register/", views.register, name="register"),
    path("auth/login/", views.login, name="login"),
    path("auth/forgot-pass/", views.forgot_pass, name="forgot_pass"),


]
