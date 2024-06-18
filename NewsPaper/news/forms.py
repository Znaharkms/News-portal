from django import forms
from .models import Post, Category
from django.core.exceptions import ValidationError


class NewForm(forms.ModelForm):
    text = forms.CharField(label="Текст поста", min_length=100, widget=forms.Textarea)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категория')

    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'user']
        labels = {
            'title': 'Заголовок',
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get("text")
    #     if description is not None and len(description) < 100:
    #         raise ValidationError({
    #             "description": "Текст не может быть менее 100 символов."
    #         })
    #
    #     return cleaned_data


if __name__ == '__main__':
    pass
