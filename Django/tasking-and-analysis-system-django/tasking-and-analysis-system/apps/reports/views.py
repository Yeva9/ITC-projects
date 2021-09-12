from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render
from .helper import get_selected_date_list, get_report_data
import xlsxwriter
from .forms import DateForm
from .manager import can_view_tab
from apps.constants import General, ReportsFields, Style
from apps.reports.models import SuccessExport
from django.contrib import messages
from apps.audit_trail.models import AuditTrail


# Exporting csv file.
# def some_view(request, farm, start_date, end_date):
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="report.csv"'},
#     )
#     writer = csv.writer(response)
#     writer.writerow([ReportsFields.FARM_NAME, General.DATE, ReportsFields.RESULT])
#     result = 0
#     count = 0
#     delta = datetime.timedelta(days=1)
#     current_date = start_date
#     while current_date <= end_date:
#         key_in_dictionary = current_date.strftime(General.DATE_FORMAT)
#         writer.writerow([farm.farm, key_in_dictionary, farm.data[key_in_dictionary]])
#
#         current_date += delta
#         count += 1
#         result += farm.data[key_in_dictionary]
#     writer.writerow([ReportsFields.AVERAGE, "", result / count])
#     return response


@login_required(login_url=General.LOGIN)
@user_passes_test(can_view_tab, login_url='/')
def reports(request):
    """
    This function is rendering report template with DateForm.
    """
    uploads = None
    form = DateForm()
    if request.method == 'POST':
        try:
            form = DateForm(request.POST)
            if form.is_valid():
                start_date = form.cleaned_data.get(General.START_DATE)
                end_date = form.cleaned_data.get(General.END_DATE)
                farm = form.cleaned_data.get(
                    ReportsFields.UPLOAD_OBJECTS_FOR_SELECTION)
                SuccessExport.objects.get_or_create()

                return download_reports_xlsx_file(request, farm, start_date,
                                                end_date)
        except Exception as exc:
            messages.error(request, "Can't export needed file. There are no data for that period of time.")
           
            log_problem_reports = AuditTrail.objects.create_log( user = str(request.user.name) 
                                                                        + "  " 
                                                                        + str(request.user.last_name),
                                                                event_title = "Unsuccessful attempt of export",
                                                                event_description = str(request.user.name)
                                                                                    + str(request.user.last_name)
                                                                                    + " Have unsuccessful attempt of exporting report, ")
            log_problem_reports.save()

    context = {
        General.SEGMENT: General.REPORTS,
        General.UPLOADS: uploads,
        General.FORM: form,
        General.ERRORS: form.errors,
        ReportsFields.REPORT_EXPORT: SuccessExport.objects.last()
    }
    return render(request, 'main_templates/reports/report.html', context)



def index(request, template_name='index.html'):

    if request.GET.get('featured'):
        featured_filter = request.GET.get('featured')
        listings = Listing.objects.filter(featured_choices=featured_filter)
    else:
        listings = Listing.objects.all()

    context_dict = {'listings': listings}
    return render(request, template_name, context_dict)

def download_reports_xlsx_file(request, farm, start_date, end_date):
    """
    This function is making xlsx file  with context manager and downloading.
    """
    response = HttpResponse(content_type=ReportsFields.CONTENT_TYPE)
    response[ReportsFields.CONTENT_DISPOSITION] = ReportsFields.ATTACHMENT
    # SuccessExport has one field with default value=today`s date
    # if object does not exist with today value
    # will be created object
    SuccessExport.objects.get_or_create()
    with xlsxwriter.Workbook(response, {Style.IN_MEMORY: True}) as workbook:
        worksheet = workbook.add_worksheet(ReportsFields.WORKSHEET_NAME)
        bold = workbook.add_format({Style.BOLD: True})
        normal_style = workbook.add_format({Style.BOLD: False})
        selected_date_set = get_selected_date_list(farm, start_date, end_date)
        data = get_report_data(farm, selected_date_set)
        for row_index, column_values in enumerate(data):
            for column_index, cell_value in enumerate(column_values):
                worksheet.write(row_index,
                                column_index,
                                str(cell_value),
                                bold if row_index == 0 else normal_style)
        log_reports = AuditTrail.objects.create_log(
            user=str(request.user.name) + "  " + str(request.user.last_name),
            event_title="Exported report",
            event_description="Export "
        )
        log_reports.save()

    return response
