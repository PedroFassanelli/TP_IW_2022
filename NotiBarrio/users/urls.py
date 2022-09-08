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

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name='password_reset_complete'),
]