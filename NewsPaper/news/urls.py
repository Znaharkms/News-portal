from django.urls import path
from .views import (PostList, PostDetail, PostSearch,
                    NewsList, NewDetail, NewCreate, NewEdit, NewDelete,
                    ArticlesList, ArticleDetail, ArticleCreate, ArticleEdit, ArticleDelete,
                    subscriptions, CategoryListView, subscribe)

urlpatterns = [
    path('main/', PostList.as_view(), name='post_list'),
    path('main/search/', PostSearch.as_view(), name='post_search'),
    path('main/<int:pk>', PostDetail.as_view(), name='post_detail'),

    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>', NewDetail.as_view(), name='new_detail'),
    path('news/create/', NewCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', NewEdit.as_view(), name='new_edit'),
    path('news/<int:pk>/delete', NewDelete.as_view(), name='new_delete'),

    path('articles/', ArticlesList.as_view(), name='articles_list'),
    path('articles/<int:pk>', ArticleDetail.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit', ArticleEdit.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),

    path('subscriptions/', subscriptions, name='subscriptions'),

]
