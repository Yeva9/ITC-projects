from django.contrib import admin
from django.urls import path, include  # add this


urlpatterns = [
    path('admin/', admin.site.urls),
    path('audit/', include("apps.audit_trail.urls")),
    path("tasks/", include("apps.tasks.urls")),
    path("reports/", include("apps.reports.urls")),
    path("upload/", include("apps.upload.urls")),  # Auth routes - login / register
    path("", include("apps.authentication.urls")),
    path("", include("apps.dashboard.urls")),

]
