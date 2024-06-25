from celery import shared_task
from django.core.mail import EmailMultiAlternatives

from .models import User
import time


@shared_task
def send_mail_new_post(pk):
    print('pk--->', pk)
    emails = User.objects.filter(
        subscriptions__category__in=pk.category.all()
    ).values_list('email', flat=True)
    print('emails', emails)

    categories = pk.category.all()
    print('categories -----> ', categories)

    subject = f"Новый пост в категории: {', '.join([f'{cat}' for cat in categories])}"

    html_content = (f'<p><b>Заголовок поста:</b> {pk.title}</p>'
                    f'<p><b>Содержание:</b> {pk.text[0:123]}</p>'
                    f'<p><b>Автор:</b> {pk.user}</p>'
                    f'<a href="http://127.0.0.1:8000{pk.get_absolute_url()}">'
                    f'Ссылка на пост</a>'
                    )
    for email in emails:
        print('email ', email)
        msg = EmailMultiAlternatives(subject, html_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
