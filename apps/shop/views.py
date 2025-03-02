from django.shortcuts import render

from apps.shop.models.product import Product
from apps.shop.models.setting import Setting

from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

# urlpatterns = [
#     path("", views.index, name="home"),
#     path("home/", views.home),
#     path("brands/", views.brand_list, name="brand_list"),
#     path("brands/<slug:slug_id>/", views.brand_products, name="brand_products"),
#     path("categories/", views.category_list, name="category_list"),
#     path("categories/<slug:slug_id>/", views.category_products, name="category_products"),
#     path("products/", views.product_list, name="product_list"),
#     path("products/<slug:slug_id>/", views.product_detail, name="product_detail"),
#     path("faq/", views.faq, name="faq"),
#     path("about/", views.about, name="about"),
#     path("contact/", views.contact, name="contact"),
#     path("auth/register/", views.register, name="register"),
#     path("auth/login/", views.login, name="login"),
#     path("auth/forgot-password/", views.forgot_password, name="forgot_password"),
# ]



def index(request):
    context = {
        "page_title": "Home",  # НА КАЖДОЙ СТРАНИЦЕ!
        "settings": Setting.objects.first(),  # НА КАЖДОЙ СТРАНИЦЕ!
        "xsro": Product.objects.all(),
    }
    return render(request, "shop/index.html", context)




def home():
    return redirect(reverse("shop:home"))









def error_404(request, exception):
    # shop/content/
    # shop/errors/
    # shop/index.html
    return render(request, "shop/errors/error_404.html")


def category_products():
    pass


def category_list():
    pass


def brand_products():
    pass


def brand_list():
    pass


def product_list():
    pass


def product_detail():
    pass


def contact():
    pass


def faq():
    pass


def about():
    pass


def register():
    pass


def login():
    pass


def forgot_password():
    pass
