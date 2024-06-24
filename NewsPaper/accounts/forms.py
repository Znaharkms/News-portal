from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives, mail_admins


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)  # Не вызывать commit сразу, чтобы мы могли изменить данные перед сохранением
        user.is_superuser = True  # Установка статуса суперпользователя. Для передачи dct[ прав группы userу, в которую он входит

        user.save()  # Сохранение пользователя с новым статусом
        authors = Group.objects.get(name="authors")  # Добавляем пользователя в группу authors
        user.groups.add(authors)

        subject = 'Добро пожаловать на наш новостной портал!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/main">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        # mail_admins(
        #     subject='Новый пользователь!',
        #     message=f'Пользователь {user.username} зарегистрировался на сайте.'
        # )

        return user
