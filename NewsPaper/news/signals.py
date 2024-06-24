from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory, Post
from django.utils import timezone


def send_notification(preview, pk, title, subscribers):
    html = render_to_string(
        'post_created_email html',
        {
            'text': preview,
            'link': f"{settings.SITE_URL}/news/{pk}"
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html, "text/html")
    msg.send()


# @receiver(m2m_changed, sender=PostCategory)
# def post_created(instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         print('categories -----> ', categories)
#         subscribers_emails = []
#         # subscription = []
#
#         for category in categories:
#             print('category ', category)
#             subscribers = Subscription.objects.filter(category=category)
#             print('subscribers ', subscribers.all())
#
#             subscribers_emails += [s.email for s in subscribers]
#
#         send_notification(instance.preview, instance.pk, instance.title, subscribers_emails)


@receiver(m2m_changed, sender=PostCategory)
def post_created(instance, **kwargs):
    if kwargs["action"] == 'post_add':
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
            msg.send()
