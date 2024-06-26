import datetime

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import User, Post, Subscription
import time


@shared_task
def send_mail_new_post(pk):
    post = Post.objects.get(id=pk)
    categories = post.category.all()

    emails = set(User.objects.filter(subscriptions__category__in=categories).values_list("email", flat=True))

    subject = f"Новый пост в категории: {', '.join([f'{cat}' for cat in categories])}"

    html_content = (f'<p><b>Заголовок поста:</b> {post.title}</p>'
                    f'<p><b>Содержание:</b> {post.text[0:123]}</p>'
                    f'<p><b>Автор:</b> {post.user}</p>'
                    f'<a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
                    f'Ссылка на пост</a>'
                    )
    for email in emails:
        print('email ', email)
        msg = EmailMultiAlternatives(subject, html_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task()
def weekly_send_emails():
    one_week_later = datetime.datetime.now() - datetime.timedelta(weeks=1)
    print('В таске weekly_send_mail')
    posts = Post.objects.filter(date__gt=one_week_later, type='AR')
    category = set(posts.values_list('category', flat=True))
    subscribers = set(Subscription.objects.filter(category__in=category).values_list('user__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts
        }
    )

    msg = EmailMultiAlternatives(
        subject=f"Статьи опубликованные за последнюю неделю",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
