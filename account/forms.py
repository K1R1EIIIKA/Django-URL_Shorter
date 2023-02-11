from django.forms import TextInput, EmailInput, CharField, PasswordInput, ModelForm, URLInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Links


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Ваш игровой никнейм'
            }),
            'email': EmailInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Пример: huykekasa@gmail.com'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-account-control'
        self.fields['password2'].widget.attrs['class'] = 'form-account-control'


class Authenticate(AuthenticationForm):
    fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(Authenticate, self).__init__(*args, **kwargs)

    username = UsernameField(widget=TextInput(
        attrs={'class': 'form-account-control',
               'placeholder': 'ник'
               }))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-account-control',
            'placeholder': 'пароль',
        }))


class CreateLink(ModelForm):
    class Meta:
        model = Links

        fields = ['full_link', 'short_link']

        widgets = {
            'full_link': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полная ссылка'
            }),
            'short_link': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сокращенная ссылка'
            })
        }
