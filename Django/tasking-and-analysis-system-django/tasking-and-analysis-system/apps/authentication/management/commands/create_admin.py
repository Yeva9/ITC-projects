from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from apps.authentication.models import User, Role


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(
                email='admin@gmail.com',
                password='admin',
                name='admin',
                last_name='admin',
                is_active=True,
                role=Role.objects.get(name='Admin')
            )
        except IntegrityError:
            print("Admin with this email already exists.")
