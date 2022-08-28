from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),

    path('email_activated/', views.email_activated, name='email_activated'),
    path('waiting_activation/', views.waiting_activation, name='waiting_activation'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]