from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Role, ServiceLocation
from ..constants import Fields, AuthenticationFields


@admin.register(ServiceLocation)
class ServiceLocationAdmin(admin.ModelAdmin):
    search_fields = [AuthenticationFields.NAME]

    def has_module_permission(self, request):
        return False

    def has_add_permission(self, request):
        return False


@admin.action(description=AuthenticationFields.ACTIVATE_SELECTED_USERS)
def activate_selected_users(modeladmin, request, queryset):
    try:
        queryset.update(is_active=True)
    except Exception:
        pass


@admin.action(description=AuthenticationFields.DEACTIVATE_SELECTED_USERS)
def deactivate_selected_users(modeladmin, request, queryset):
    try:
        queryset.update(is_active=False)
    except Exception:
        pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = [
        AuthenticationFields.NAME,
        AuthenticationFields.LAST_NAME,
        AuthenticationFields.EMAIL,
        AuthenticationFields.ROLE,
        AuthenticationFields.SERVICE_LOCATION,
    ]

    def service_locations(self, obj):
        return ", ".join([str(p) for p in obj.service_location.all()])

    autocomplete_fields = [AuthenticationFields.SERVICE_LOCATION]

    list_display_links = [AuthenticationFields.EMAIL]

    list_display = [
        AuthenticationFields.NAME,
        AuthenticationFields.LAST_NAME,
        AuthenticationFields.EMAIL,
        AuthenticationFields.ROLE,
        AuthenticationFields.IS_ACTIVE,
        AuthenticationFields.SERVICE_LOCATION_LIST_DISPLAY
    ]
    actions = [activate_selected_users, deactivate_selected_users]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    # filter_horizontal = (AuthenticationFields.PERMISSIONS,)

    fieldsets = (
        (None,
         {
             Fields.FIELDS:
                 (Fields.NAME,)
         }),
    )
    readonly_fields = [AuthenticationFields.NAME]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.unregister(Group)
