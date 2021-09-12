from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
from .manager import *
from .models import *
from .forms import TaskForm
from apps.dashboard.views import pages, error403
from apps.constants import General, TaskFields
from apps.constants import UserRoles
from .helper import get_task_xlsx, validate_readonly_fields, home
from django.contrib import messages


@login_required(login_url=General.LOGIN)
@user_passes_test(can_view_tab, login_url='/')
def tasks_view(request):
    visible_tasks = get_user_visible_tasks(request.user)

    if request.method == "POST":
        if visible_tasks.count() > 0:
            return get_task_xlsx(request.user, visible_tasks)
        else:
            messages.error(request, "Error: No data to download.")
    context = {
        General.SEGMENT: General.TASKS,
        General.TASKS: visible_tasks,
    }
    return render(
        request,
        'main_templates/tasks/task_index.html',
        context
    )


@login_required(login_url=General.LOGIN)
@user_passes_test(can_view_tab, login_url='/')
def create(request, parent_id=None, farm_id=None):
    parent_task = None
    if parent_id:
        # should be created sub-task
        try:
            parent_task = get_task_by_id(parent_id)
            if parent_task.assigned_to != request.user or \
                    request.user.role.name == UserRoles.TASK_EXECUTOR:
                return error403(request)
        except Exception:
            return pages(request)
        form_initial_data = {
            TaskFields.PID: parent_id,
            TaskFields.ASSIGNED_BY: request.user.name 
                                    + " "
                                    + request.user.last_name,
            TaskFields.CREATED_DATE: datetime.today(),
            TaskFields.SUBSTATION: parent_task.substation,
        }
        readonly_fields = [TaskFields.PID, TaskFields.ASSIGNED_BY,
                           TaskFields.SUBSTATION,
                           TaskFields.CURRENT_READABILITY,
                           TaskFields.CREATED_DATE]
        readonly_dict = {field: getattr(parent_task, field)
                         for field in readonly_fields}
        readonly_dict[TaskFields.ASSIGNED_BY] = request.user
        readonly_dict[TaskFields.CREATED_DATE] = datetime.today()
    else:
        # should be created parent task
        if request.user.role.name != UserRoles.TASK_CREATOR:
            return error403(request)
        if farm_id:
            try:
                farm = Upload.objects.get(id=farm_id)
            except Exception:
                return redirect(pages(request))
            form_initial_data = {
                TaskFields.ASSIGNED_BY: request.user.name 
                                        + " " 
                                        + request.user.last_name,
                TaskFields.CREATED_DATE: datetime.today(),
                TaskFields.SUBSTATION: farm,
            }

            readonly_dict = {
                TaskFields.ASSIGNED_BY: request.user,
                TaskFields.CURRENT_READABILITY: 0,
                TaskFields.CREATED_DATE: datetime.today(),
                TaskFields.SUBSTATION: farm,
            }
        else:
            form_initial_data = {
                TaskFields.ASSIGNED_BY: request.user.name 
                                        + " " 
                                        + request.user.last_name,
                TaskFields.CREATED_DATE: datetime.today(),
            }

            readonly_dict = {
                TaskFields.ASSIGNED_BY: request.user,
                TaskFields.CURRENT_READABILITY: 0,
                TaskFields.CREATED_DATE: datetime.today(),
            }

    queryset = get_executors(parent_id is not None)
    form = TaskForm(
        initial=form_initial_data, 
        queryset=queryset,
        is_readonly_substation=(parent_task is not None or farm_id is not None)
    )

    if request.method == 'POST':
        request_dict = request.POST.copy()
        print(request_dict)
        request_dict[TaskFields.ASSIGNED_BY] = request.user
        request_dict[TaskFields.TASK_TITLE] = TaskFields.TITLE_TEXT.format(
            request_dict[TaskFields.TARGET_READABILITY]
        )
        form = TaskForm(
            validate_readonly_fields(readonly_dict, request_dict),
            queryset=queryset,
            is_readonly_substation=(parent_task is not None or farm_id is not None)
        )
        if parent_task:
            request_dict[TaskFields.SUBSTATION] = parent_task.substation
        elif farm_id:
            request_dict[TaskFields.SUBSTATION] = farm
        if form.is_valid():
            task = form.save()
            if not parent_id:
                task.pid = task.id
                task.save(update_fields=[TaskFields.PID])
            return redirect(General.TASKS)
    context = {
        General.SEGMENT: [General.TASKS, General.CREATE],
        General.FORM: form,
        General.PARENT_TASK: parent_task,
        General.ERRORS: form.errors,
    }
    return render(
        request,
        'main_templates/tasks/task_create_or_edit.html',
        context,
    )


@login_required(login_url=General.LOGIN)
@user_passes_test(can_view_tab, login_url='/')
def edit(request, task_id):
    try:
        task = get_task_by_id(task_id)
        if task.assigned_by != request.user and not \
                task.assigned_to == request.user:
            return error403(request)
    except Exception:
        return pages(request)
    
    add_readonlies = (request.user != task.assigned_by)
    if add_readonlies:
        readonly_dict = {field.name: getattr(task, field.name)
                         for field in task._meta.fields}
        readonly_dict.pop(TaskFields.PROGRESS)
    else:
        readonly_fields = [TaskFields.PID, TaskFields.ASSIGNED_BY,
                           TaskFields.SUBSTATION,
                           TaskFields.CURRENT_READABILITY,
                           TaskFields.CREATED_DATE]
        readonly_dict = {field: getattr(task, field)
                         for field in readonly_fields}

    form = TaskForm(
        instance=task,
        initial={
            TaskFields.ASSIGNED_BY: task.assigned_by.name +
            " " + task.assigned_by.last_name,
        },
        add_readonlies=add_readonlies,
        queryset=get_executors(task_id != task.pid)
        if request.user.role.name != UserRoles.TASK_EXECUTOR else None,
        is_readonly_substation=True
    )
    if request.method == 'POST':
        request_dict = request.POST.copy()
        request_dict[TaskFields.ASSIGNED_BY] = task.assigned_by
        request_dict[TaskFields.TASK_TITLE] = TaskFields.TITLE_TEXT.format(
            request_dict[TaskFields.TARGET_READABILITY]
        )
        request_dict[TaskFields.SUBSTATION] = task.substation
        if request.user != task.assigned_by:
            request_dict[TaskFields.ASSIGNED_TO] = task.assigned_to
        form = TaskForm(
            validate_readonly_fields(readonly_dict, request_dict),
            instance=task,
            add_readonlies=request.user != task.assigned_by,
            queryset=get_executors(task_id != task.pid)
            if request.user.role.name != UserRoles.TASK_EXECUTOR else None,
            is_readonly_substation=True
        )
        if form.is_valid():
            form.save()
            return redirect(General.TASKS)
    context = {
        General.SEGMENT: [General.TASKS, General.EDIT],
        General.FORM: form,
        TaskFields.TASK_ID: task_id,
        General.ERRORS: form.errors,
    }
    return render(
        request,
        'main_templates/tasks/task_create_or_edit.html',
        context
    )
