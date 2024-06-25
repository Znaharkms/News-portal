from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        # pass
        # отключил импорт для реализации задачи через Celery
        from . import signals  # выполнение модуля -> регистрация сигналов
