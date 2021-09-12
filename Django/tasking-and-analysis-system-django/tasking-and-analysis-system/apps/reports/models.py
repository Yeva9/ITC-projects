from datetime import date
from django.db import models


class Report(models.Model):
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'


class SuccessExport(models.Model):
    objects = None
    export_date = models.DateField(default=date.today)
