from datetime import datetime

from django.db import models
from django.utils import timezone


class AuditTrailManager(models.Manager):
    def create_log(self, user, event_title,
                   event_description):
        log = self.create(user=user, event_title=event_title,
                          event_description=event_description,
                          event_date=datetime.now())
        return log


class AuditTrail(models.Model):
    user = models.TextField(
                            blank=False)
    event_title = models.TextField(
                            blank=False)
    event_description = models.TextField()
    event_date = models.DateTimeField(
                            default=timezone.now)
    objects = AuditTrailManager()

    def __str__(self):
        return self.event_title

    class Meta:
        ordering = ["-id"]
