"""Vympel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', include('content.urls')), # Отслеживание вт. ссылок с прилож. content
    path('reg/', userViews.register, name="reg"), # Страница регистрации
    path('feedback/', userViews.feedback, name="feedback"), # Обратная связь
    path('introduction/', userViews.introduction, name="introduction"), # Страница регистрации
    path('auth/', authViews.LoginView.as_view(template_name='users/auth.html' ), name="auth"), # Страница авторизации
    path('pass-reset/', authViews.PasswordResetView.as_view(template_name='users/pass_reset.html' ), name="pass-reset"), # Страница восстановления пароля
    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html' ), name="password_reset_complete"), # Страница восстановления пароля
    path('password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html' ), name="password_reset_confirm"), # Страница восстановления пароля
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html' ), name="password_reset_done"), # Страница восстановления пароля
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html' ), name="exit"), # Страница выхода из учетной записи
    path('admin/', admin.site.urls), # Администратирование
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
