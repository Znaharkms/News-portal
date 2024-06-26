from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory, Subscription
from .tasks import send_mail_new_post
from django.utils import timezone


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if kwargs["action"] == 'post_add':
        send_mail_new_post.delay(instance.pk)


"""     Эта часть кода перенесена в tasks -> send_mail_new_post
        emails = User.objects.filter(
            subscriptions__category__in=instance.category.all()
        ).values_list('email', flat=True)
        categories = instance.category.all()

        subject = f"Новый пост в категории: {', '.join([f'{cat}' for cat in categories])}"

        html_content = (f'<p><b>Заголовок поста:</b> {instance.title}</p>'
                        f'<p><b>Содержание:</b> {instance.text[0:123]}</p>'
                        f'<p><b>Автор:</b> {instance.user}</p>'
                        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
                        f'Ссылка на пост</a>'
                        )
        for email in emails:
            print('***********email ', email)
            msg = EmailMultiAlternatives(subject, html_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()"""
