from django.apps import AppConfig


class AuditTrailConfig(AppConfig):
    name = 'apps.audit_trail'

    def ready(self):
        import apps.audit_trail.signals