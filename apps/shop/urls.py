from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
	path("home/", views.index)
]