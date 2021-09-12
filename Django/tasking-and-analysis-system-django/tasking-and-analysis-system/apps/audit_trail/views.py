from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.audit_trail.models import AuditTrail
from apps.constants import General, AuthenticationFields, UserRoles
from apps.dashboard.views import error403


@login_required(login_url=AuthenticationFields.LOGIN)
def audit_view(request):
    if request.user.role.name != UserRoles.ADMIN:
        return error403(request)
    audit = AuditTrail.objects.all()
    context = {
        General.SEGMENT: General.AUDIT,
        General.AUDIT: audit,
    }
    return render(request,
                  'main_templates/audit/audit_trail.html',
                  context)
