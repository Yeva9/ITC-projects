from django.urls import path
from .views import audit_view

urlpatterns = [
    path('', audit_view, name="audit")
]