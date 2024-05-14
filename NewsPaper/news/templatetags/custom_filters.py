from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def length(value):
    """
    value: значение, к которому нужно применить фильтр
    """
    # Возвращаемое функцией значение подставится в шаблон.
    return len(value)


@register.filter()
def censor(value):
    list_crensor = ['редиск', 'дурак', 'дурынд']
    for word in list_crensor:
        if word in value.lower():
            value = value.replace(word[1:], (len(word) - 1) * '*')
    return value
