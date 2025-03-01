from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.home),
    path("brands/", views.brand_list, name="brand_list"),
    path("brands/<slug:slug_id>/", views.brand_products, name="brand_products"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/<slug:slug_id>/", views.category_products, name="category_products"),
    path("products/", views.product_list, name="product_list"),
    path("products/<slug:slug_id>/", views.product_detail, name="product_detail"),
    path("faq/", views.faq, name="faq"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("auth/register/", views.register, name="register"),
    path("auth/login/", views.login, name="login"),
    path("auth/forgot-password/", views.forgot_password, name="forgot_password"),
]
