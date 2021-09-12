from django.contrib.auth.models import Permission

from .authentication.models import User


def __get_user_group_permissions(user_id):
    """
    This function returns user permissions based on his/her role(group).
    """
    try:
        user = User.objects.get(id=user_id)
        permissions = Permission.objects.filter(group__id=user.role_id)
        user_perms = [perm.codename for perm in permissions]
        return user_perms

    except Exception as exc:
        return []
