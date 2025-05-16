import stripe
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from .models import EmailOTP
from .forms import EmailForm, OTPForm
from django.utils import timezone

def send_otp(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = f'{random.randint(100000, 999999)}'

            # Сохраняем OTP в БД
            EmailOTP.objects.create(email=email, code=code)

            # Отправляем письмо
            send_mail(
                subject='Ваш OTP код',
                message=f'Ваш код подтверждения: {code}',
                from_email=None,
                recipient_list=[email],
                fail_silently=False,
            )
            return redirect(reverse("payments:verify_otp"))
    else:
        form = EmailForm()
    return render(request, 'payments/send_otp.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = form.cleaned_data['code']

            try:
                otp_record = EmailOTP.objects.filter(email=email, code=code, is_used=False).latest('created_at')
            except EmailOTP.DoesNotExist:
                otp_record = None

            if otp_record and not otp_record.is_expired():
            # Вместо пометки is_used — сразу удаляем
                otp_record.delete()
                # Здесь можно делать логин или другое действие
                return render(request, 'payments/success.html')
            else:
                form.add_error(None, 'Неверный или просроченный код')
    else:
        form = OTPForm()
    return render(request, 'payments/verify_otp.html', {'form': form})







stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Test Product',
                    },
                    'unit_amount': 1000,  # 10.00 USD
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/payments/success/',
            cancel_url='http://localhost:8000/payments/cancel/',
        )
        return JsonResponse({'id': session.id})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def success(request):
    return render(request, 'payments/success.html')

def cancel(request):
    return render(request, 'payments/cancel.html')

# views.py
def checkout(request):
    return render(request, 'payments/checkout.html')
