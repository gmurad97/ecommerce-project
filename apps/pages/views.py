from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Setting, Category


# Create your views here.
def index(request):
    # "settings": Setting.objects.first(), - check this line try catche exception....if object exitst this object send error

    context = {
        "categories": {# должно быть везде примечение: высокий
            "all": Category.objects.all(),  # Все категории
            "navbar": Category.objects.all()[:5],  # 5 категорий для навбара
        },
        "page_title": "Home",  # должно быть везде примечение: высокий (Заголовок страницы)
        "settings": Setting.objects.first(),  # должно быть везде примечение: высокий
        "breadcrumbs":[
            {"name": "url", "name": "url"}
        ]
    }
    return render(request, "pages/index.html", context)


def home():
    return redirect(reverse("pages:home"))


def product_list():
    pass


def product_detail():
    pass


def category_list(request):
    context = {
        "categories": Category.objects.all(),
        "page_title": "Home",  # должно быть везде примечение: высокий (Заголовок страницы)
        "settings": Setting.objects.first(),  # должно быть везде примечение: высокий
    }
    return render(request, "pages/index.html",context)


def category_products(request,slug_id):
    context = {
        "categories": Category.objects.all(),
        "page_title": "Home",  # должно быть везде примечение: высокий (Заголовок страницы)
        "settings": Setting.objects.first(),  # должно быть везде примечение: высокий
    }
    return render(request, "pages/index.html",context)


def about():
    pass


def contacts():
    pass


def faq():
    pass


def gallery():
    pass


def register():
    pass


def login():
    pass


def error_404(request, exception):
    pass

    # path("", views.index, name="home"),
    # path("home/", views.home),
    # path("about/", views.about, name="about"),
    # path("contacts/", views.contacts, name="contacts"),
    # path("faq/", views.faq, name="faq"),
    # path("gallery/", views.gallery, name="gallery"),
    # path("categories/", views.category_list, name="category_list"),
    # path("categories/<slug:slug_id>", views.category_products, name="category_products"),
    # path("products/", views.product_list, name="product_list"),
    # path("products/<slug:slug_id>", views.product_detail, name="product_detail"),
    # path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
