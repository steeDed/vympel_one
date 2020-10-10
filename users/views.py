from django.shortcuts import render, redirect
from .forms import UserOurRegistrationForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import IntroductionForm, Feedback

# Регистрация
def register(request):
    if request.method == "POST":
        form = UserOurRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} успешно создан, введите имя и пароль для авторизации')
            return redirect ('auth')
    else:
        form = UserOurRegistrationForm()
    return render(request, 'users/registration.html', {'title': 'Регистрация', 'form': form})

def introduction(request):
    if request.method == "POST":
        form = IntroductionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Заявка успешно отправлена, ожидайте ответа')
            return redirect ('main')
    else:
        form = IntroductionForm()
    return render(request, 'users/introduction.html', {'title': 'Заявка на вступление', 'form': form})
# Обратная связь
def feedback(request):
    if request.method == "POST":
        form = Feedback(request.POST)
        if form.is_valid():
            message = request.POST.get('message', '')
            email = request.POST.get('email', '')

            send_mail(email, message, email, ['help32yuanarmyvympel@gmail.com'], fail_silently=False)
            messages.success(request, f'Письмо успешно отправлено, ожидайте ответа')
            return redirect('main')
    else:
        form = Feedback()

    return render(request, 'users/feedback.html', {'form': form})
