from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path(
        "create-checkout-session/",
        views.create_checkout_session,
        name="create_checkout_session",
    ),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("checkout/", views.checkout, name="checkout"),
    path("send-otp/", views.send_otp, name="send_otp"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
]
