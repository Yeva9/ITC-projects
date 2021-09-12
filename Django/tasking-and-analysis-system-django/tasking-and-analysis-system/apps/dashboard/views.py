import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db import ProgrammingError
from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse
from django.template import loader
from openpyxl import Workbook

from apps.audit_trail.models import AuditTrail
from apps.authentication.models import User
from apps.constants import General, AuthenticationFields, DashboardFields, ReportsFields
from apps.reports.models import SuccessExport
from apps.tasks.models import Task
from apps.upload.models import Upload, UploadSuccess
from .helper import get_day_statistic, get_day_readability, \
                    get_avg_readability, get_task_progress_count, \
                    export_data_to_xlsx, export_logs_to_xlsx
from .manager import can_view_tab


@login_required(login_url=AuthenticationFields.LOGIN)
def index(request):
    if request.method == "POST":
        if request.user.role.name == 'Task creator':
            return export_data_to_xlsx(request)
        elif request.user.role.name == 'Admin':
            return export_logs_to_xlsx(request)

    users = User.objects.all()
    uploads = Upload.objects.all()[:11]

    all_logins = AuditTrail.objects.filter(event_description='User login')
    login_statistics = []
    end_date = datetime.date.today()
    current_date = datetime.date(end_date.year, end_date.month, 1)
    delta = datetime.timedelta(days=1)
    while current_date <= end_date:
        login_statistics.append(get_day_statistic(current_date, all_logins))
        current_date += delta

    audit = AuditTrail.objects.all().order_by('-id')[:10]
    try:
        export = SuccessExport.objects.last()
    except ProgrammingError:
        export = None

    progress_cnt = get_task_progress_count(request)

    context = {
        General.USERS: users,
        General.SEGMENT: General.INDEX,
        DashboardFields.ALL_USER_COUNT: User.objects.count(),
        DashboardFields.ACTIVE_USER_COUNT: User.objects.filter(is_active=True).count(),
        DashboardFields.UPLOADS: uploads,
        DashboardFields.SUCCESS_UPLOADS: UploadSuccess.objects.last(),
        DashboardFields.TASK_IN_PROGRESS: progress_cnt['count1'],
        DashboardFields.TASK_COMPLETED: progress_cnt['count2'],
        DashboardFields.TASK_REJECTED: progress_cnt['count3'],
        DashboardFields.TASK_TOTAL: progress_cnt['count4'],

        General.AUDIT: audit,
        ReportsFields.REPORT_EXPORT: export,
        # for admin's chart
        'login_stat': login_statistics,
        # for task creator's chart
        'avg_readability': get_avg_readability(uploads),
        'day_readability': get_day_readability(uploads)
    }
    return render(request, 'main_templates/index.html', context)


@user_passes_test(can_view_tab, login_url='/')
@login_required(login_url=General.LOGIN)
def view_more(request):
    if request.method == "POST":
        return export_logs_to_xlsx(request)

    users = User.objects.all()
    audit = AuditTrail.objects.all()

    context = {
        'users': users,
        'audit': audit,
        'segment': 'index',
    }

    return render(request, 'main_templates/view_more.html', context)


@login_required(login_url=AuthenticationFields.LOGIN)
def pages(request):
    context = {}

    html_template = loader.get_template('page-404.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url=General.LOGIN)
def error403(request):
    context = {}

    html_template = loader.get_template('page-403.html')
    return HttpResponse(html_template.render(context, request))
