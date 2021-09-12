from django.db import models
from apps.authentication.models import User
from apps.upload.models import Upload


class Progress(models.Model):
    """
    Intended to show the current status of the task. Can be
    'New', 'In progress', 'Rejected', 'Complete'
    """
    name = models.CharField(
        max_length=15
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Progress'
        verbose_name_plural = 'Progress'


class Task(models.Model):
    objects = None
    pid = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    assigned_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="task_creator"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="task_executor"
    )
    progress = models.ForeignKey(
        Progress,
        on_delete=models.CASCADE
    )
    created_date = models.DateField()
    due_date = models.DateField()
    task_title = models.CharField(
        max_length=30
    )
    task_description = models.TextField(
        blank=True
    )
    substation = models.ForeignKey(
        Upload,
        on_delete=models.PROTECT
    )
    current_readability = models.SmallIntegerField(
        default=0
    )
    target_readability = models.SmallIntegerField(
        default=100
    )

    def __str__(self):
        return self.task_title

    class Meta:
        ordering = []
        verbose_name = "Task"
        verbose_name_plural = "Tasks"







   
