from datetime import datetime

from django.shortcuts import render

from .models import *
from apps.constants import General, UploadFields
from django.contrib import messages


def get_or_update_upload_instance(xlsx_file, last_upload):
    fields = [field.lower().replace(' ', '_') for field in xlsx_file[3]]
    readability1 = fields[5]
    readability2 = fields[6]
    readability3 = fields[7]
    for row in xlsx_file[4:]:
        if len(row) < len(fields):
            continue
        region, _ = Region.objects.get_or_create(
            name=row[fields.index(General.REGION)]
        )
        upload, created = Upload.objects.get_or_create(
            farm=row[fields.index(General.FARM)],
            region=region,
        )
        upload.upload_date = datetime.strptime(row[fields.index(General.DATE)], UploadFields.UPLOAD_DATE_FORMAT) if row[
            fields.index(General.DATE)] else None
        upload.cows_count = row[fields.index(UploadFields.COWS_COUNT)]
        upload.alive_cows_count = row[fields.index(UploadFields.ALIVE_COWS_COUNT)] if row[
            fields.index(UploadFields.ALIVE_COWS_COUNT)] else 0
        upload.data[readability1] = row[fields.index(readability1)] if str(
            row[fields.index(readability1)]).isdigit() else 0
        upload.data[readability2] = row[fields.index(readability2)] if str(
            row[fields.index(readability2)]).isdigit() else 0
        upload.data[readability3] = row[fields.index(readability3)] if str(
            row[fields.index(readability3)]).isdigit() else 0
        upload.save()
        last_upload = upload
    return last_upload

