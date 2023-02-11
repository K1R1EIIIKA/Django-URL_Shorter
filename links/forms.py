from django.forms import TextInput, ModelForm, URLInput
from .models import Links


class CreateLink(ModelForm):
    class Meta:
        model = Links

        fields = ['full_link', 'short_link']

        widgets = {
            'full_link': URLInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Введите ссылку'
            }),
            'short_link': TextInput(attrs={
                'class': 'form-account-control',
                'placeholder': 'Введите текст'
            })
        }
