from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Rejestracja(UserCreationForm):
    username = forms.CharField(label="",
                               max_length=50, help_text="<small class='form-text text-muted'>Wymagana. 150 lub mniej znaków. Jedynie litery, cyfry i @/./+/-/_.</small>", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa użytkownika'}))
    name = forms.CharField(label="",
                                 max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię'}))
    surname = forms.CharField(label="",
                                max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko'}))
    email = forms.EmailField(label="",
                             max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adres e-mail'}))
    password1 = forms.CharField(label="", help_text="<small><ul class='form-text text-muted'><li>Twoje hasło nie może być zbyt podobne do twoich innych danych osobistych.</li><li>Twoje hasło musi zawierać co najmniej 8 znaków.</li><li>Twoje hasło nie może być powszechnie używanym hasłem.</li><li>Twoje hasło nie może składać się tylko z cyfr.</li></ul></small>",
                                max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}))
    password2 = forms.CharField(label="", help_text="<small class='form-text text-muted'>Wprowadź to samo hasło ponownie, dla weryfikacji.</small>",
                                max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Potwtórz hasło'}))

    class Meta:
        model = User
        fields = ['username', 'name', 'surname',
                  'email', 'password1', 'password2']


