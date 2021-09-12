from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'apps.authentication'

    def ready(self):
        import apps.authentication.signals
