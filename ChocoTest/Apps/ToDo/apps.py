from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.ToDo'
    verbose_name = "ToDo"

    def ready(self):
        import Apps.ToDo.signals