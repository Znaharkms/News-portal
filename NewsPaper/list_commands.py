'''''

In [1]: from news.models import *

In [2]: u1 = User.objects.create_user(username='Andrey')

In [3]: u2 = User.objects.create_user(username='Maxim')

In [4]: a1 = Author.objects.create(user=u1)

In [5]: a2 = Author.objects.create(user=u2)

In [6]: ca1 = Category.objects.create(category='Политика')

In [7]: ca2 = Category.objects.create(category='"Экономикаа')

In [8]: ca3 = Category.objects.create(category='"Юмор')

In [9]: ca4 = Category.objects.create(category='Спорт')

In [11]: p1 = Post.objects.create(type='article', user=a1, title='Политика и спорт', text='Политика и спорт или спортивная диплома
    ...: тия описывает использование спорта как средства влияния на дипломатические, социальные и политические отношения.')

In [12]: p2 = Post.objects.create(type='article', user=a2, title='Бюджет', text='Бюджет все равно, что совесть: от расходов он не
    ...: удерживает, но вызывает чувство вины.')

In [13]: p3 = Post.objects.create(type='news', user=a2, title='Узнавшая о беременности американка родила через 15 минут', text='Жи
    ...: тельница США приняла боль в животе за аппендицит и приехала в больницу, где ей сказали о том, что она беременна. Женщина
    ...: родила через 15 минут.')

In [14]: p1.category.add(ca1)

In [15]: p1.category.add(ca3)

In [17]: p2.category.add(ca2)

In [18]: p2.category.add(ca3)

In [19]: p1.category.add(ca4)

In [20]: p3.category.add(ca1)

In [21]: p3.category.add(ca3)

In [22]: c1 = Comment.objects.create(user=a1.user, comment=p1, text='Умно!')

In [23]: c2 = Comment.objects.create(user=a1.user, comment=p2, text='Ха-ха! Интересно!')

In [24]: c3 = Comment.objects.create(user=a1.user, comment=p2, text='Бывает же такое!')

In [25]: c4 = Comment.objects.create(user=a2.user, comment=p1, text='А говорят спорт вне политики...')

In [26]: c5 = Comment.objects.create(user=a2.user, comment=p2, text='Хы-хы! Очень смешно!')

In [27]: c6 = Comment.objects.create(user=a2.user, comment=p3, text='Абалдеть!')

In [28]: p1.like()

In [29]: p2.like()

In [30]: p3.like()

In [31]: c3.like()

In [32]: c1.like()

In [34]: c5.dislike()

In [35]: c6.like()

In [36]: c4.like()

In [38]: c3.like()

In [39]: p1.like()

In [40]: p2.like()

In [41]: p3.like()

In [42]: p1.dislike()

In [43]: c6.like()

In [44]: c5.like()

In [45]: c3.dislike()

In [47]: a1.update_rating()

In [48]: a1.rating
Out[48]: 7

In [51]: a2.update_rating()

In [52]: a2.rating
Out[52]: 18

In [59]: srt1 = Author.objects.all().order_by('rating').values('user__username','rating')

In [60]: srt1
Out[60]: <QuerySet [{'user__username': 'Andrey', 'rating': 7}, {'user__username': 'Maxim', 'rating': 18}]>

In [61]: srt1.last()
Out[61]: {'user__username': 'Maxim', 'rating': 18}

ИЛИ сортировать в обратном порядке и взять первый объект
In [63]: Author.objects.all().order_by('-rating').values('user__username','rating')[0]
Out[63]: {'user__username': 'Maxim', 'rating': 18}

In [64]: post = Post.objects.all().order_by('-rating').values('date', 'user__user__username','rating', 'title', 'text'[:124])[0]
Out[64]:
{'date': datetime.datetime(2024, 5, 10, 14, 45, 21, 616363, tzinfo=datetime.timezone.utc),
 'user__user__username': 'Maxim',
 'rating': 2,
 'title': 'Бюджет',
 'text': 'Бюджет все равно что совесть: от расходов он не удерживает, но вызывает чувство вины. Жить по бюджету – то же самое, что жить не по средствам, с той только разницей, что все аккуратно заносится на бумагу.'}

In [65]: Post.objects.order_by('-rating')[0].comment_set.all().values('date', 'user__username', 'rating', 'text')
Out[65]: <QuerySet [{'date': datetime.datetime(2024, 5, 10, 15, 2, 52, 446773, tzinfo=datetime.timezone.utc),
'user__username': 'Andrey',
'rating': 0, 'text': 'Ха-ха! Интересно!'},
{'date': datetime.datetime(2024, 5, 10, 15, 3, 24, 779706, tzinfo=datetime.timezone.utc),
'user__username': 'Andrey',
'rating': 1,
'text': 'Бывает же такое!'},
{'date': datetime.datetime(2024, 5, 10, 15, 5, 34, 175468, tzinfo=datetime.timezone.utc),
'user__username': 'Maxim',
'rating': 0,
'text': 'Хы-хы! Очень смешно!'}]'''
