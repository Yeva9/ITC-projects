"""
A Manager is the interface through which database query operations are provided to Django models.
"""

from django.contrib.auth.base_user import BaseUserManager
from ..constants import AuthenticationFields


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''
            Create and save a user with the given email, and
            password.
        '''
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user = user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault(AuthenticationFields.IS_STAFF, False)
        extra_fields.setdefault(AuthenticationFields.IS_SUPERUSER, False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault(AuthenticationFields.IS_STAFF, True)
        extra_fields.setdefault(AuthenticationFields.IS_SUPERUSER, True)
        if extra_fields.get(AuthenticationFields.IS_STAFF) is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )
        return self._create_user(email, password, **extra_fields)
