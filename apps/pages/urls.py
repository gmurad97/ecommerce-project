from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.index, name="home"),

    path("register/", views.index, name="register"),
    path("login/", views.index, name="login"),
    path("", views.index, name="home"),
    path("", views.index, name="home"),
    path("", views.index, name="home"),
    path("", views.index, name="home"),
    path("", views.index, name="home"),
]
