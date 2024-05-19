from django.urls import path
from .views import (PostList, PostDetail, NewsList, NewDetail, NewCreate,
                    ArticlesList, ArticleDetail, ArticleCreate)

urlpatterns = [
    path('main/', PostList.as_view(), name='post_list'),
    path('main/<int:pk>', PostDetail.as_view(), name='post_detail'),

    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewDetail.as_view(), name='new_detail'),
    path('news/create/', NewCreate.as_view(), name='news_create'),

    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
]
