from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import UserManager
from ..constants import AuthenticationFields


class Role(Group):
    class Meta:
        proxy = True
        verbose_name = AuthenticationFields.ROLE


class ServiceLocation(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = AuthenticationFields.SERVICE_LOCATION_LIST_DISPLAY


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=100,
        unique=True
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.RESTRICT,
        related_name=AuthenticationFields.ROLE,
        # null=True
        blank=True
    )
    is_active = models.BooleanField(
        default=False,
        db_index=True
    )
    service_location = models.ManyToManyField(
        ServiceLocation,
        related_name=AuthenticationFields.SERVICE_LOCATION_LIST_DISPLAY,
    )
    date_registered = models.DateTimeField(default=timezone.now)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = AuthenticationFields.EMAIL
    objects = UserManager()

    def __str__(self):
        return str(self.name) + " " + str(self.last_name)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        fields = kwargs.pop('update_fields', [])
        if fields != ['last_login']:
            return super(User, self).save(*args, **kwargs)


