from django.core.management.base import BaseCommand
from apps.constants import Progress as ProgressValues
from apps.tasks.models import Progress


class Command(BaseCommand):
    def handle(self, *args, **options):
        for progress in ProgressValues.PROGRESS:
            Progress.objects.get_or_create(name=progress)
