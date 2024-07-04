from django.apps import AppConfig


class LendingConfig(AppConfig):
    verbose_name = "Store database"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lending'