from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.urls import reverse
from apps.shop.models import Product, Setting, Category, Brand

def get_base_context():
    categories_with_products = Category.objects.annotate(products_count=Count("products")).filter(products_count__gt=0)
    
    return {
        "settings": Setting.objects.first(),
        "categories": {
            "all": categories_with_products,
            "searchbar": Category.objects.all(),
            "navbar": Category.objects.all(),
            "home_last": categories_with_products[:10],  # Новая логика
        },
        "brands": {
            "all": Brand.objects.all(),
            "navbar": Brand.objects.all(),
        },
    }



def index(request):
    context = get_base_context()
    context.update(
        {
            "page_title": "Home",
            "products": {
                "all": Product.objects.all().select_related("category", "brand"),
                "home_last": Product.objects.all().order_by("-id")[:10],
            },
            "with_slider": True,
        }
    )
    return render(request, "shop/index.html", context)


def home():
    return redirect(reverse("shop:index"))


def category_list(request):
    return render(
        request,
        "shop/contents/categories.html",
        {**get_base_context(), "page_title": "Categories", "with_slider": False},
    )


def category_products(request, slug_id):
    category = get_object_or_404(Category, slug=slug_id)
    context = get_base_context()
    context.update(
        {
            "page_title": category.name,
            "products": Product.objects.filter(category=category).select_related("brand"),
            "with_slider": False,
        }
    )
    return render(request, "shop/contents/category_products.html", context)


def brand_list(request):
    return render(
        request, "shop/contents/brands.html", {**get_base_context(), "page_title": "Brands", "with_slider": False}
    )


def brand_products(request, slug_id):
    brand = get_object_or_404(Brand, slug=slug_id)
    context = get_base_context()
    context.update(
        {
            "page_title": brand.name,
            "products": Product.objects.filter(brand=brand).select_related("category"),
            "with_slider": False,
        }
    )
    return render(request, "shop/contents/brand_products.html", context)


def product_list(request):
    return render(
        request,
        "shop/contents/products.html",
        {
            **get_base_context(),
            "page_title": "Products",
            "products": Product.objects.all().select_related("category", "brand"),
            "with_slider": False,
        },
    )


def product_detail(request, slug_id):
    product = get_object_or_404(Product, slug=slug_id)
    return render(
        request,
        "shop/contents/product_detail.html",
        {**get_base_context(), "page_title": product.name, "product": product, "with_slider": False},
    )


def contact(request):
    return render(
        request, "shop/contents/contact.html", {**get_base_context(), "page_title": "Contact", "with_slider": False}
    )


def faq(request):
    return render(request, "shop/contents/faq.html", {**get_base_context(), "page_title": "FAQ", "with_slider": False})


def about(request):
    return render(
        request, "shop/contents/about.html", {**get_base_context(), "page_title": "About", "with_slider": False}
    )


def register(request):
    return render(
        request,
        "shop/contents/auth/register.html",
        {**get_base_context(), "page_title": "Register", "with_slider": False},
    )


def login(request):
    return render(
        request, "shop/contents/auth/login.html", {**get_base_context(), "page_title": "Login", "with_slider": False}
    )


def forgot_password(request):
    return render(
        request,
        "shop/contents/auth/forgot_password.html",
        {**get_base_context(), "page_title": "Forgot Password", "with_slider": False},
    )


def error_404(request, exception=None):
    return render(
        request, "shop/errors/error_404.html", {**get_base_context(), "page_title": "Error 404", "with_slider": False}
    )
