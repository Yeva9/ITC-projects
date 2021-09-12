from django.urls import path
from .views import tasks_view, edit, create
from apps.constants import General

urlpatterns = [
    path('', tasks_view, name=General.TASKS),
    path('create/<int:parent_id>/', create, name=General.SUBTASK_CREATE),
    path('create/by-farm/<int:farm_id>/', create, name='create_by_farm'),
    path('create/', create, name=General.TASK_CREATE),
    path('edit/<int:task_id>/', edit, name=General.TASK_EDIT),
]
