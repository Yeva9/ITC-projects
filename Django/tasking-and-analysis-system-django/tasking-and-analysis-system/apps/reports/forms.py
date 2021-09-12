from datetime import datetime

from django import forms
from apps.reports.models import Report
from apps.tasks.forms import DateInput
from apps.upload.models import Upload
from .helper import get_selected_date_list
from apps.constants import General, Errors, Style, ReportsFields
from apps.audit_trail.models import AuditTrail


class DateForm(forms.ModelForm):
    """
    This is class for form of DateForm, which has the following fields:
    - upload objects: ModelChoiceField
    - start date: DateInput
    - end date: DateInput
    """

    upload_objects_for_selection = forms.ModelChoiceField(
        queryset=Upload.objects.all(),
        widget=forms.Select(
            attrs={
                Style.CLASS: ReportsFields.CSS_FOR_DROPDOWN,
                Style.STYLE: Style.SELECT_STYLE
            })
    )

    class Meta:
        model = Report
        fields = [General.START_DATE,
                  General.END_DATE]
        widgets = {
            General.START_DATE: DateInput(
                attrs=ReportsFields.MIN_MAX_DATES_OF_DATE_DROPDOWN
            ),
            General.END_DATE: DateInput(
                attrs=ReportsFields.MIN_MAX_DATES_OF_DATE_DROPDOWN
            ),
        }

    def clean(self):
        """

        This is overridden clean() method, which is responsible for
        validation in the correct order  and propagating their errors.
        Here we get selected start date, end date. After comparing
        of start date and end date program will show errors in each case.

        :return: selected data from user
        """

        super().clean()
        cleaned_data = self.cleaned_data
        start_date = cleaned_data.get(General.START_DATE)
        end_date = cleaned_data.get(General.END_DATE)
        selected_upload_object = cleaned_data[
            ReportsFields.UPLOAD_OBJECTS_FOR_SELECTION]
        existing_date_keys = selected_upload_object.data.keys()
        selected_date_list = get_selected_date_list(selected_upload_object,
                                                    start_date,
                                                    end_date)
        if start_date > end_date:
            self._errors[Errors.CONVERSION_ERROR] = self.error_class(
                [Errors.CONVERSION_ERROR_MESSAGE])
            log_data_error = AuditTrail.objects.create_log(user=str(self.name),
                                                           event_title="Unsuccesful attempt of exporting report",
                                                           event_description=str(
                                                               self.name) + "  tryed to export report with invalide date")
            log_data_error.save()
        elif len(set(selected_date_list) & set(existing_date_keys)) == 0:
            self._errors[Errors.OUT_OF_RANGE_ERROR] = self.error_class(
                [Errors.OUT_OF_RANGE_ERROR_MESSAGE])
            log_data_range_error = AuditTrail.objects.create_log(user=str(self.name),
                                                                 event_title="Unsuccesful attempt of exporting report",
                                                                 event_description=str(
                                                                     self.name) + "  tryed to export report with invalide date")
            log_data_range_error.save()

        return cleaned_data
