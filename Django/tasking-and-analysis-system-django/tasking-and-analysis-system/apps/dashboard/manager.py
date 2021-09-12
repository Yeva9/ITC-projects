"""
A Manager is the interface through which database query operations are provided to Django models.
"""

from apps.authentication.user_permissions import Permissions
from ..manager import __get_user_group_permissions


def can_view_tab(user):
    return Permissions.CAN_VIEW_ADMIN_PAGE[0]  in \
           __get_user_group_permissions(user.id)
