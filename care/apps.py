from django.apps import AppConfig


class CareConfig(AppConfig): # copy CareConfig and pst it in settings.py on the template
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'care'
