from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import FormSignUp
from NotiBarrio import settings


def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_to = request.GET.get('next')
                if redirect_to is None:
                    return redirect('homepage')
                else:
                    return redirect(redirect_to)
    return render(request, "login.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = FormSignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            user = User.objects.create_user(username, email, password)
            user.is_active = False
            user.save()

            try:
                token = default_token_generator.make_token(user)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                mail_subject = "NotiBarrio - Activación de cuenta"
                message = render_to_string('email_activation.html', {
                    'user': user,
                    'domain': domain,
                    'uid': uidb64,
                    'token': token,
                })
                email_host = settings.EMAIL_HOST_USER
                send_mail(mail_subject, message, email_host, [email])
                return render(request, 'waiting_activation.html')
            except Exception as e:
                messages.error(request, f"No se pudo enviar el correo para la activación de la cuenta")
    else:
        form = FormSignUp()
    return render(request, "signup.html", {"form": form})


def waiting_activation(request):
    return render(request, 'waiting_activation.html')


def email_activated(request):
    return render(request, 'email_activated.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None:
        if user.is_active:
            return redirect('login')
        user.is_active = True
        user.save()
        return render(request, "email_activated.html")
    else:
        messages.error(request, f"El enlace de activación no es válido")
    return redirect("login")


@login_required(login_url='/login/')
def logout_user(request):
    auth.logout(request)
    messages.success(request,"Se ha cerrado la sesión")
    return redirect('/')