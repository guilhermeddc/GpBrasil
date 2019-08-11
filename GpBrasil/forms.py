from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    Nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu Nome"
            }
        )
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu e-mail"
            }
        )
    )
    Mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Sua Mensagem"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('Email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('Email has to be gmail.com')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario',
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "login"
                                   }
                               )
                               )
    password = forms.CharField(label='Senha',
                               widget=forms.PasswordInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "senha"
                                   }
                               )
                               )


class RegisterForm(forms.Form):
    username = forms.CharField(label='Usuario',
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "Usuario"
                                   }
                               )
                               )
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(
                                 attrs={
                                     "class": "form-control",
                                     "placeholder": "E-mail"
                                 }
                             )
                             )
    password = forms.CharField(label='Senha',
                               widget=forms.PasswordInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "senha"
                                   }
                               )
                               )
    confirm_password = forms.CharField(label='Confirmar Senha',
                                       widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "confirmar senha"
        }
    ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('E-mail is taken')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError('Passwords must match.')
        return data
