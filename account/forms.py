from django.forms import TextInput, EmailInput, CharField, PasswordInput, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-account-control',
            }),
            'email': EmailInput(attrs={
                'class': 'form-account-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-account-control'
        del self.fields['password2']


class Authenticate(AuthenticationForm):
    fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(Authenticate, self).__init__(*args, **kwargs)

    username = UsernameField(widget=TextInput(
        attrs={'class': 'form-account-control',
               }))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-account-control',
        }))


class UserUpdateForm(ModelForm):
    class Meta:
        model = User

        fields = ['username', 'email']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Введите имя пользователя'
            }),
            'email': EmailInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Введите почту'
            })
        }
