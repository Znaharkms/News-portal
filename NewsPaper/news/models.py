from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce


# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user

    def update_rating(self):
        post_rating = self.post.aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        comments_rating = self.user.comment.aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        post_comments_rating = self.post.aggregate(pcr=Coalesce(Sum('comment__rating'), 0))[
            'pcr']

        self.rating = post_rating * 3 + comments_rating + post_comments_rating
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=100, default='article', unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    categor = [
        ('article', 'Статья'),
        ('news', 'Новость'),
    ]
    type = models.CharField(max_length=10, choices=categor, default=article)
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post')
    category = models.ManyToManyField(Category, through='PostCategory')
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def preview(self):
        return self.text[:124] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)  #
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')  #
    text = models.TextField()  #
    date = models.DateTimeField(auto_now_add=True)  #
    rating = models.SmallIntegerField(default=0)  #

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
