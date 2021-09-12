from django.db import models
from datetime import date


class Region(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Upload(models.Model):
    """
    Saves information from the downloaded files.
    """
    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT
    )
    farm = models.CharField(max_length=100)
    # as of 10.08.21 this field is unknown
    upload_date = models.DateField(blank=True, null=True)
    cows_count = models.IntegerField(null=True)
    alive_cows_count = models.IntegerField(null=True)
    # Dictionary with keys of current day and values of current day's data
    data = models.JSONField(default=dict)
    objects = None

    def __str__(self):
        return self.farm


class UploadSuccess(models.Model):
    objects = None
    upload_date = models.DateField(default=date.today)
    last_upload = models.ForeignKey(Upload, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.upload_date) + " " + str(self.last_upload)
