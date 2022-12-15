from django.apps import AppConfig


class ReportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'report'
    verbose_name = 'Отчет'
    verbose_name_plural = 'Отчеты'
