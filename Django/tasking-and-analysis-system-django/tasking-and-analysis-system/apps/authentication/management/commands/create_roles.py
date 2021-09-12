from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from apps.authentication.models import Role
from apps.authentication.user_permissions import Permissions
from apps.constants import UserRoles

GROUPS = {
    UserRoles.ADMIN: [
        Permissions.CAN_VIEW_ADMIN_PAGE[0],
        Permissions.CAN_ADD_USERS[0],
        Permissions.CAN_DELETE_USERS[0],
        Permissions.CAN_DEACTIVATE_USERS[0],
        Permissions.CAN_EDIT_USER_INFORMATION[0],
        Permissions.CAN_EXPORT_LOG_FILES[0]
    ],

    UserRoles.ANALYST: [
        Permissions.CAN_VIEW_UPLOAD_PAGE[0],
        Permissions.CAN_VIEW_REPORTS_PAGES[0],
        Permissions.CAN_UPLOAD_FILES_INTO_THE_SYSTEM[0],
        Permissions.CAN_GENERATE_REPORTS[0],
        Permissions.CAN_EXPORT_XLSX_FILES[0]
    ],

    UserRoles.TASK_EXECUTOR: [
        Permissions.CAN_VIEW_TASKS_PAGE[0],
        Permissions.CAN_VIEW_ONLY_ASSIGNED_SUBTASKS[0],
        Permissions.CAN_VIEW_TASK_COUNTS_ACCORDING_TO_STATUSES[0],
        Permissions.CAN_EDIT_ASSIGNED_TASKS_ONLY_STATUS_FIELD[0]
    ],

    UserRoles.TASK_DISTRIBUTOR: [
        Permissions.CAN_VIEW_TASKS_PAGE[0],
        Permissions.CAN_VIEW_TASKS_TAB[0],
        Permissions.CAN_VIEW_TASK_LIST[0],
        Permissions.CAN_ADD_NEW_SUBTASK[0],
        Permissions.CAN_EDIT_OWN_SUBTASK[0],
        Permissions.CAN_ASSIGN_SUBTASK_TO_USER_WITH_ROLE_TASK_EXECUTOR[0]
    ],

    UserRoles.TASK_CREATOR: [
        Permissions.CAN_VIEW_TASKS_PAGE[0],
        Permissions.CAN_VIEW_TASKS_TAB[0],
        Permissions.CAN_VIEW_TASK_LIST[0],
        Permissions.CAN_VIEW_ONLY_USERS_WITH_ROLE_TASKS_DISTRIBUTOR[0],
        Permissions.CAN_CREATE_NEW_TASK[0],
        Permissions.CAN_ASSIGN_TASK_TO_THE_USER_WITH_TASK_DISTRIBUTOR_ROLE[0],
        Permissions.CAN_EDIT_OWN_TASKS[0]
    ]
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        for group in GROUPS:
            new_group, _ = Role.objects.get_or_create(name=group)
            for permission in GROUPS[group]:
                content_type = ContentType.objects.get(app_label="authentication", model='role')
                permission_obj, _ = Permission.objects.get_or_create(
                    codename=permission,
                    name=permission,
                    content_type=content_type
                )
                new_group.permissions.add(permission_obj)

                new_group.save()
