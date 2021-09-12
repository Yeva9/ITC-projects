from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from pyexcel_xlsx import get_data as xlsx_get
from .manager import can_view_tab
from .models import *
from apps.constants import General, UploadFields, AuthenticationFields
from zipfile import BadZipfile
from django.contrib import messages
from .helper import get_or_update_upload_instance
from apps.audit_trail.models import AuditTrail


@csrf_protect
@login_required(login_url=AuthenticationFields.LOGIN)
@user_passes_test(can_view_tab, login_url='/')
def upload_file(request):
    if request.method == 'POST':
        try:
            files_dict = dict(request.FILES)
            files = files_dict[General.FILE]
            for file in files:
                xlsx_file = xlsx_get(file)
                sheet = list(xlsx_file.keys())[0]
                xlsx_file = xlsx_file[sheet]
                last_upload = None
                last_upload = get_or_update_upload_instance(xlsx_file, last_upload)
                if last_upload:
                    UploadSuccess.objects.create(last_upload=last_upload)
            messages.success(request, "Success")

            logUpload = AuditTrail.objects.create_log(user=str(request.user.name)
                                                           + " "
                                                           + str(request.user.last_name),
                                                      event_title="Upload",
                                                      event_description="Uploaded file")
            logUpload.save()
        except Exception as exc:
            messages.error(request, "Error: File does not match.")
            LogTryUpload = AuditTrail.objects.create_log(user=str(request.user.name)
                                                              + " "
                                                              + str(request.user.last_name),
                                                         event_title="Unsuccesful attempt of upload",
                                                         event_description="Unsuccesful attempt of upload")
            LogTryUpload.save()
    context = {
        General.SEGMENT: UploadFields.UPLOAD,
        UploadFields.SUCCESS_UPLOADS: UploadSuccess.objects.last(),
    }
    return render(
        request,
        'main_templates/upload/upload.html',
        context
    )
