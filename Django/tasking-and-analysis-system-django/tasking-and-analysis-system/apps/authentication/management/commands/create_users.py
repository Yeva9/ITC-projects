from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from apps.authentication.models import User, Role


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:

            User.objects.create_superuser(
                email='analyst@yopmail.com',
                password='admin',
                name='analyst',
                last_name='analyst',
                is_active=True,
                role=Role.objects.get(name='Analyst')
            )

            User.objects.create_superuser(
                email='task_distributor@yopmail.com',
                password='admin',
                name='task',
                last_name='distributor',
                is_active=True,
                role=Role.objects.get(name='Task distributor')
            )

            User.objects.create_superuser(
                email='task_creator@yopmail.com',
                password='admin',
                name='task',
                last_name='creator',
                is_active=True,
                role=Role.objects.get(name='Task creator')
            )

            User.objects.create_superuser(
                email='task_executor@yopmail.com',
                password='admin',
                name='task',
                last_name='executor',
                is_active=True,
                role=Role.objects.get(name='Task executor')
            )

        except IntegrityError:
            print("User with this email already exists.")
