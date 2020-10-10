from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Introduction
class UserOurRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class IntroductionForm(forms.ModelForm):
    class Meta:
        model = Introduction
        fields = ('name', 'klass', 'phone', 'email')

class Feedback(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(label="Текст сообщения", widget = forms.Textarea)
