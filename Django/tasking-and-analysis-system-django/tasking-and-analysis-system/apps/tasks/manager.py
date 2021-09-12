"""
A Manager is the interface through which database query operations are provided to Django models.
"""

from apps.authentication.user_permissions import Permissions
from ..manager import __get_user_group_permissions
from .models import Task
from apps.authentication.models import User, Role
from apps.constants import UserRoles, TaskFields


def can_view_tab(user):
    return Permissions.CAN_VIEW_TASKS_PAGE[0] in __get_user_group_permissions(
        user.id)


def get_task_by_id(task_id):
    return Task.objects.get(id=task_id)


def get_user_visible_tasks(user):
    tasks = Task.objects.filter(assigned_by=user) | \
            Task.objects.filter(assigned_to=user)
    tasks = tasks.order_by(TaskFields.ID)

    # only distributer can see parent and sub tasks
    if user.role.name == UserRoles.TASK_DISTRIBUTOR:
        last_pid = None
        sorted_tasks = Task.objects.none()
        for task in tasks:
            if task.pid != last_pid:
                last_pid = task.pid
                sorted_tasks |= (Task.objects.filter(pid=last_pid) & tasks)

        return sorted_tasks.order_by('pid', 'id')
    else:
        return tasks


def get_executors(is_subtask):
    if is_subtask:
        # get users with role TASK_EXECUTOR
        return User.objects.filter(role=Role.objects.get(
            name=UserRoles.TASK_EXECUTOR))
    else:
        # get users with role TASK_DISTRIBUTOR
        return User.objects.filter(role=Role.objects.get(
            name=UserRoles.TASK_DISTRIBUTOR))
