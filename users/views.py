from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

from .utils import generate_code


SESSION_EXPIRE_TIME = 60 * 15  # 15 daqiqa


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').lower().strip()
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {
                'error': 'Bu email allaqachon ishlatilgan'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {
                'error': 'Bu username band'
            })

        code = generate_code()

        # eski sessionni tozalaymiz
        request.session.flush()

        request.session['verify_code'] = code
        request.session['register_data'] = {
            'username': username,
            'email': email,
            'password': password
        }

        try:
            send_mail(
                subject="BusterDev — Email tasdiqlash kodi",
                message=(
                    "Assalomu alaykum!\n\n"
                    "Ro‘yxatdan o‘tishni tasdiqlash kodingiz:\n\n"
                    f"{code}\n\n"
                    "Agar bu amalni siz bajarmagan bo‘lsangiz, "
                    "xabarni e’tiborsiz qoldiring.\n\n"
                    "Hurmat bilan,\n"
                    "BusterDev jamoasi"
                ),
                from_email="BusterDev <yourgmail@gmail.com>",
                recipient_list=[email],
                fail_silently=False,
            )
        except Exception:
            return render(request, 'users/register.html', {
                'error': 'Email yuborilmadi. Keyinroq urinib ko‘ring.'
            })

        return redirect('verify_email')

    return render(request, 'users/register.html')


def verify_email(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        if code != request.session.get('verify_code'):
            return render(request, 'users/verify_email.html', {
                'error': 'Kod noto‘g‘ri'
            })

        data = request.session.get('register_data')
        if not data:
            messages.error(request, "Session muddati tugagan. Qayta ro‘yxatdan o‘ting.")
            return redirect('register')

        if User.objects.filter(username=data['username']).exists():
            messages.info(request, "Bu akkaunt allaqachon tasdiqlangan.")
            return redirect('login')

        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        # sessionni yangilab login qilamiz
        request.session.flush()
        login(request, user)
        request.session.set_expiry(SESSION_EXPIRE_TIME)

        messages.success(request, "Email tasdiqlandi! Xush kelibsiz 👋")
        return redirect('home')

    return render(request, 'users/verify_email.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session.set_expiry(SESSION_EXPIRE_TIME)
            return redirect('home')

        return render(request, 'users/login.html', {
            'error': 'Username yoki parol xato'
        })

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')