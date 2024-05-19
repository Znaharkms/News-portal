from django.forms import DateTimeInput, CharField, ModelChoiceField, ModelMultipleChoiceField
from django.db.models import DateField
from django_filters import FilterSet, DateTimeFilter
from .models import Post, Category
from django import forms
from django_filters import rest_framework as filters


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    date = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        label='Дата:',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = Post

        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = {'title', 'category', 'date'}

    # fields = {
    # поиск по названию
    # 'title': ['icontains'],
    # по дате
    # 'date': ['gte'],
    # по категории
    # 'category': ['exact'],
    # }


if __name__ == '__main__':
    pass
