import inspect

from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_protect
from .models import AuditTrail
from apps.constants import AuditTrailConstants, TaskFields
from apps.authentication.models import User
from apps.tasks.models import Task
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=Task)
def LogTasks(sender, instance, created, **kwargs):
    if kwargs[TaskFields.UPDATE_FIELDS]:
        if TaskFields.PID in set(kwargs[TaskFields.UPDATE_FIELDS]):
            return
    if created:
        if not instance.pid:
            new_task = AuditTrail.objects.create_log(
                                user=str(instance.assigned_by),
                                event_title=AuditTrailConstants.CREATED_TASK,
                                event_description=AuditTrailConstants.NEW_TASK_CREATED)
            new_task.save()
        else:
            subtask = AuditTrail.objects.create_log(
                                user=str(instance.assigned_by),
                                event_title=AuditTrailConstants.CREATED_SUBTASK,
                                event_description=AuditTrailConstants.NEW_SUBTASK_CREATED.format(str(instance.id)))

            subtask.save()
    else:
        updated_task = AuditTrail.objects.create_log(
            user=str(instance.assigned_by),
            event_title=AuditTrailConstants.UPDATED_TASK,
            event_description=AuditTrailConstants.UPDATED_TASK_INFO.format(str(instance.id), str(instance.progress.name)))
        updated_task.save()

@csrf_protect
@receiver(post_save, sender=User)
def logsCreateUpdateUser(sender, instance, created, **kwargs):
    if created:
        new_user = AuditTrail.objects.create_log(
            user=str(instance.name) 
                    + " " 
                    + str(instance.last_name),
            event_title=AuditTrailConstants.CREATED_NEW_USER,
            event_description=AuditTrailConstants.CREATED_USER_INFO.format(str(instance.name), str(instance.last_name)))
    else:
        new_user = AuditTrail.objects.create_log(
            user =str(instance.name) 
                    + " " 
                    + str(instance.last_name),
            event_title=AuditTrailConstants.UPDATED_USER,
            event_description=AuditTrailConstants.UPDATED_USER_INFO.format(str(instance.name), str(instance.last_name)))
    new_user.save()


@csrf_protect
@receiver(user_logged_in, sender=User)
def user_login(sender, request, user, **kwarg):
    new_log = AuditTrail.objects.create_log(
        user=str(user.name) 
                + " " 
                + str(user.last_name),
        event_title=AuditTrailConstants.USER_LOGIN,
        event_description=AuditTrailConstants.USER_LOGIN)
    new_log.save()


@csrf_protect
@receiver(user_logged_out, sender=User)
def user_logout(sender, request, user, **kwarg):
    logout = AuditTrail.objects.create_log(
        user=str(user.name) 
                + " " 
                + str(user.last_name),
        event_title=AuditTrailConstants.USER_LOGOUT,
        event_description=AuditTrailConstants.USER_LOGOUT)
    logout.save()


@receiver(user_login_failed)
def login_failed(sender, credentials, **kwargs):
    try:
        login_fail = AuditTrail.objects.create_log(
            user = str( User.objects.get(email = str(credentials.get('username')))),
            event_title=AuditTrailConstants.LOGIN_FAILED,
            event_description=AuditTrailConstants.WRONG_PASSWORD)
    except ObjectDoesNotExist:
        login_fail = AuditTrail.objects.create_log(
            user = str(credentials.get('username')),
            event_title = AuditTrailConstants.LOGIN_FAILED,
            event_description = AuditTrailConstants.USER_DOES_NOT_EXIST)

    login_fail.save()
