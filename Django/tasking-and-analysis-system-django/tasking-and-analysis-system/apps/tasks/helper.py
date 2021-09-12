import io

from django.shortcuts import render
import xlsxwriter
from django.http import HttpResponse
from apps.constants import TaskFields, Style
from apps.audit_trail.models import AuditTrail
from django.contrib import messages


def validate_readonly_fields(readonly_dict, request_dict):
    for field in request_dict.keys():
        if field in readonly_dict.keys():
            request_dict[field] = readonly_dict[field]

    return request_dict


def get_data(tasks):
    data = [[
        TaskFields.PID.capitalize(),
        TaskFields.ID.capitalize(),
        TaskFields.SUBSTATION.capitalize(),
        TaskFields.ASSIGNED_BY.capitalize().replace('_', ' '),
        TaskFields.ASSIGNED_TO.capitalize().replace('_', ' '),
        TaskFields.CURRENT_READABILITY.capitalize().replace('_', ' '),
        TaskFields.TASK_TITLE.capitalize().replace('_', ' '),
        TaskFields.TASK_DESCRIPTION.capitalize().replace('_', ' '),
        TaskFields.CREATED_DATE.capitalize().replace('_', ' '),
        TaskFields.DUE_DATE.capitalize().replace('_', ' '),
        TaskFields.PROGRESS.capitalize(),
    ]]
    for task in tasks:
        data.append([
        task.pid,
        task.id,
        task.substation,
        task.assigned_by,
        task.assigned_to,
        task.current_readability,
        task.task_title,
        task.task_description,
        task.created_date,
        task.due_date,
        task.progress,
    ])

    return data


def get_task_xlsx(user, tasks):
    
    data = get_data(tasks)

    output = io.BytesIO()

    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    bold = workbook.add_format({Style.BOLD: True})
    unbold = workbook.add_format({Style.BOLD: False})

    for row_num, columns in enumerate(data):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num, col_num, str(cell_data), bold
                            if row_num == 0 else unbold)

    # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)
    response = HttpResponse(
        output,
        content_type='application/'
                     'vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={'Content-Disposition': 'attachment; filename="tasks.xlsx"'},
    )
    LogDownloadedTask = AuditTrail.objects.create_log( user = str(user.name) + str(user.last_name),
                                                            event_title = "Downloaded tasks list",
                                                            event_description = str(user.name) 
                                                                                + str(user.last_name)
                                                                                + " have downloaded task_list")
    LogDownloadedTask.save()
    return response


def home(request):
    data = dict()
    messages.success(request,
                     "Success: This is the sample success Flash message.")
    messages.error(request, "Error: This is the sample error Flash message.")
    messages.info(request, "Info: This is the sample info Flash message.")
    messages.warning(request,
                     "Warning: This is the sample warning Flash message.")
    return render(
        request,
        'main_templates/tasks/task_index.html',
        data)
