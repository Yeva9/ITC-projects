from django import forms
from django.db.models.query import QuerySet
from .models import Task, Progress
from apps.constants import Style, TaskFields, General, Progress as PR
from apps.upload.models import Upload


def get_progress_queryset(current_progress):
    if current_progress == PR.REJECTED or current_progress == PR.COMPLETED:
        return Progress.objects.filter(name=current_progress)
    elif current_progress == PR.NEW:
        return Progress.objects.all()
    else:
        queryset = Progress.objects.none()
        for progress in Progress.objects.all():
            if progress.name != PR.NEW:
                queryset |= Progress.objects.filter(name=progress.name)
        
        return queryset


def add_readonly_fields(fields):
    fields[TaskFields.ASSIGNED_TO].widget.attrs[Style.STYLE] += \
        Style.READONLY_STYLE
    fields[TaskFields.ASSIGNED_TO].widget.attrs[Style.DISABLED] = Style.DISABLED
    fields[TaskFields.SUBSTATION].widget.attrs[Style.STYLE] += \
        Style.READONLY_STYLE
    fields[TaskFields.SUBSTATION].widget.attrs[Style.DISABLED] = Style.DISABLED
    fields[TaskFields.ASSIGNED_TO].required = False
    fields[TaskFields.TARGET_READABILITY].widget.attrs[Style.STYLE] += \
        Style.READONLY_STYLE
    fields[TaskFields.TARGET_READABILITY].widget.attrs[Style.READONLY] = \
        Style.READONLY
    fields[TaskFields.DUE_DATE].widget.attrs[Style.STYLE] += \
        Style.READONLY_STYLE
    fields[TaskFields.DUE_DATE].widget.attrs[Style.READONLY] = Style.READONLY
    fields[TaskFields.TASK_DESCRIPTION].widget.attrs[Style.STYLE] += \
        Style.READONLY_STYLE
    fields[TaskFields.TASK_DESCRIPTION].widget.attrs[Style.READONLY] = \
        Style.READONLY


def check_other_var(kwargs):
    """
    This function will get and return variables, 
    which are not in kwargs by default,
    and delete from kwargs
    """
    queryset = None
    add_readonlies = False
    is_readonly_substation = True
    if General.QUERYSET in kwargs.keys():
        queryset = kwargs[General.QUERYSET]
        kwargs.pop(General.QUERYSET)
    if General.ADD_READONLIES in kwargs.keys():
        add_readonlies = kwargs[General.ADD_READONLIES]
        kwargs.pop(General.ADD_READONLIES)
    if General.IS_READONLY_SUBSTATION in kwargs.keys():
        is_readonly_substation = kwargs[General.IS_READONLY_SUBSTATION]
        kwargs.pop(General.IS_READONLY_SUBSTATION)
    
    return queryset, add_readonlies, is_readonly_substation


class DateInput(forms.DateInput):
    input_type = General.DATE


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        queryset, add_readonlies, is_readonly_substation = \
            check_other_var(kwargs)

        super().__init__(*args, **kwargs)
        self.fields[TaskFields.PID].required = False
        self.fields[TaskFields.ASSIGNED_BY].required = False
        self.fields[TaskFields.SUBSTATION].required = False
        self.fields[TaskFields.TASK_DESCRIPTION].required = False
        self.fields[TaskFields.SUBSTATION].queryset = Upload.objects.all()
        self.fields[TaskFields.PROGRESS].empty_label = None
        if 'instance' not in kwargs.keys():
            self.fields[TaskFields.PROGRESS].initial = \
                Progress.objects.get(name='New')
            self.task_id = None
        else:
            self.task_id = kwargs['instance'].id
            self.fields[TaskFields.PROGRESS].initial = \
                kwargs['instance'].progress
        if not isinstance(queryset, type(None)):
            self.fields[TaskFields.ASSIGNED_TO].queryset = queryset

        self.add_readonlies = False
        if add_readonlies:
            self.add_readonlies = True
            add_readonly_fields(self.fields)
        elif is_readonly_substation:
            self.fields[TaskFields.SUBSTATION].widget.attrs[Style.STYLE] += \
                Style.READONLY_STYLE
            self.fields[TaskFields.SUBSTATION].widget.attrs[Style.DISABLED] = \
                Style.DISABLED

        self.fields[TaskFields.PROGRESS].queryset = \
            get_progress_queryset(self.fields[TaskFields.PROGRESS].initial.name)

    class Meta:
        model = Task
        fields = [TaskFields.PID, TaskFields.ASSIGNED_BY,
                  TaskFields.ASSIGNED_TO, TaskFields.TASK_TITLE,
                  TaskFields.TASK_DESCRIPTION, TaskFields.CREATED_DATE,
                  TaskFields.DUE_DATE, TaskFields.PROGRESS,
                  TaskFields.SUBSTATION, TaskFields.CURRENT_READABILITY,
                  TaskFields.TARGET_READABILITY]
        widgets = {
            TaskFields.PID: forms.NumberInput(
                attrs={
                    Style.READONLY: Style.READONLY,
                    Style.STYLE: Style.READONLY_STYLE + Style.WHOLE_STYLE +
                                 Style.WIDTH_100,
                }
            ),
            TaskFields.ASSIGNED_BY: forms.TextInput(
                attrs={
                    Style.READONLY: Style.READONLY,
                    Style.STYLE: Style.READONLY_STYLE + Style.WHOLE_STYLE +
                                 Style.WIDTH_100,
                }
            ),
            TaskFields.ASSIGNED_TO: forms.Select(
                attrs={
                    Style.CLASS: Style.FORM_CONTROL,
                    Style.STYLE: Style.WHOLE_STYLE + Style.WIDTH_100,
                }
            ),
            TaskFields.TASK_TITLE: forms.TextInput(),
            TaskFields.TASK_DESCRIPTION: forms.Textarea(                
                attrs={
                    Style.CLASS: Style.FORM_CONTROL,
                    Style.STYLE: 'resize: none;' + Style.WHOLE_STYLE +
                                 Style.WIDTH_100,
                    Style.ROWS: 4, Style.COLS: 35
                }
            ),
            TaskFields.PROGRESS: forms.Select(
                attrs={
                    Style.STYLE: Style.WHOLE_STYLE + Style.WIDTH_100,
                }
            ),
            TaskFields.SUBSTATION:forms.Select(
                attrs={
                    Style.CLASS: Style.FORM_CONTROL,
                    Style.STYLE: Style.WHOLE_STYLE + Style.WIDTH_100,
                }
            ),
            TaskFields.CURRENT_READABILITY: forms.NumberInput(
                attrs={
                    Style.READONLY: Style.READONLY,
                    Style.MIN: 0, Style.MAX: 100,
                    Style.STYLE: Style.WIDTH_90 + Style.WHOLE_STYLE
                    + Style.READONLY_STYLE,
                }
            ),
            TaskFields.TARGET_READABILITY: forms.NumberInput(
                attrs={
                    Style.MIN: 0, Style.MAX: 100,
                    Style.STYLE: Style.WIDTH_90 + Style.WHOLE_STYLE
                }
            ),
            TaskFields.CREATED_DATE: DateInput(
                attrs={
                    Style.READONLY: Style.READONLY,
                    Style.STYLE: Style.WIDTH_100 + Style.WHOLE_STYLE +
                    Style.READONLY_STYLE
                }
            ),
            TaskFields.DUE_DATE: DateInput(
                attrs={
                    Style.STYLE: Style.WIDTH_100 + Style.WHOLE_STYLE
                }
            ),
        }

    def clean(self):
        super(TaskForm, self).clean()

        due_date = self.cleaned_data.get(TaskFields.DUE_DATE)
        created_date = self.cleaned_data.get(TaskFields.CREATED_DATE)

        if due_date < created_date:
            self._errors[TaskFields.DUE_DATE] = \
                self.error_class(['Choose valid date'])

        target_readability = \
            self.cleaned_data.get(TaskFields.TARGET_READABILITY)
        current_readability = \
            self.cleaned_data.get(TaskFields.CURRENT_READABILITY)

        if target_readability <= current_readability:
            self._errors[TaskFields.TARGET_READABILITY] = \
                self.error_class(['Type valid readability'])
        
        if not self.cleaned_data.get(TaskFields.SUBSTATION):
            self._errors[TaskFields.SUBSTATION] = \
                self.error_class(['Substation is required field'])
        
        return self.cleaned_data
