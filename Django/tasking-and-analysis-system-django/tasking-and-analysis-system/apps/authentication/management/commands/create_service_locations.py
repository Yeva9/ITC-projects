from django.core.management.base import BaseCommand
from apps.authentication.models import ServiceLocation
from apps.constants import ServiceLocationsConstants


class Command(BaseCommand):
    def handle(self, *args, **options):
        for service_location in ServiceLocationsConstants.SERVICE_LOCATIONS:
            ServiceLocation.objects.get_or_create(name=service_location)

