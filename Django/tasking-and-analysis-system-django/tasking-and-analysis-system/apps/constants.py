from datetime import datetime

from cryptography.fernet import Fernet


# general constants
class General:
    ID = 'id'
    USERS = 'users'
    QUERYSET = 'queryset'
    ADD_READONLIES = 'add_readonlies'
    SEGMENT = 'segment'
    TASKS = 'tasks'
    SHOW_TASKS = 'show_tasks'
    SHOW_SUBTASKS = 'show_subtasks'
    TASK_CREATE = 'task_create'
    TASK_EDIT = 'task_edit'
    SUBTASK_CREATE = 'subtask_create'
    CREATE = 'create'
    EDIT = 'edit'
    DATE = 'date'
    FORM = 'form'
    LOGIN = 'login'
    START_DATE = 'start_date'
    END_DATE = 'end_date'
    DATA = 'data'
    FARM = 'farm'
    REGION = 'region'
    REPORTS = 'reports'
    REPORT = 'report'
    ERRORS = 'errors'
    UPLOADS = 'uploads'
    DATE_FORMAT = '%d.%m.%Y'
    MESSAGE = 'message'
    HOME = 'home'
    DATETIME_FORMAT = "%Y/%m/%d %H:%M:%S"
    PARENT_TASK = 'parent_task'
    FILE = 'file'
    CLASS = 'class'
    AUDIT = 'audit'
    INDEX = 'index'
    IS_READONLY_SUBSTATION = 'is_readonly_substation'


class DashboardFields:
    ALL_USER_COUNT = 'all_user_count'
    ACTIVE_USER_COUNT = 'active_user_count'
    UPLOADS = 'uploads'
    SUCCESS_UPLOADS = 'success_uploads'
    TASK_IN_PROGRESS = 'task_in_progress'
    TASK_COMPLETED = 'task_completed'
    TASK_REJECTED = 'task_rejected'
    TASK_TOTAL = 'task_total'
    VIEW_MORE = 'view_more'


class UploadFields:
    COWS_COUNT = 'cows_count'
    ALIVE_COWS_COUNT = 'alive_cows_count'
    UPLOAD = 'upload'
    SUCCESS_UPLOADS = 'success_uploads'
    UPLOAD_DATE_FORMAT = '%d.%m.%Y %H:%M:%S'


class AuthenticationFields:
    NAME = 'name'
    LAST_NAME = 'last_name'
    EMAIL = 'email'
    IS_ACTIVE = 'is_active'
    SERVICE_LOCATION = 'service_location'
    DATE_REGISTERED = 'date_registered'
    PERMISSIONS = 'permissions'
    ACTIVATE_SELECTED_USERS = 'Activate selected Users'
    DEACTIVATE_SELECTED_USERS = 'Deactivate selected Users'
    SERVICE_LOCATION_LIST_DISPLAY = 'service_locations'
    DATE_FORMAT = "%d.%m.%Y"
    IS_STAFF = 'is_staff'
    IS_SUPERUSER = 'is_superuser'
    PASSWORD = 'password'
    PASSWORD1 = 'password1'
    PASSWORD2 = 'password2'
    PASSWORD_CHECK = 'password check'
    LOGIN = 'login'
    ROLE = 'role'

    EMAIL_SEND_FORM = 'email_send_form'


# style constants
class Style:
    WHOLE_STYLE = ('border-radius: 5px; padding: 5px; '
                   'border: 1px solid rgb(241, 241, 241);'
                   ' color: black; background: white;')
    READONLY_STYLE = 'background: rgb(241, 241, 241) !important;'
    SELECT_STYLE = 'border: 1px solid #4FC3F7; border-radius: .25rem; background: white;'
    READONLY = 'readonly'
    STYLE = 'style'
    CLASS = 'class'
    FORM_CONTROL = 'form_control'
    ROWS = 'rows'
    COLS = 'cols'
    MIN = 'min'
    IN_MEMORY = 'in_memory'
    MAX = 'max'
    BOLD = 'bold'
    DISABLED = 'disabled'
    PLACEHOLDER = 'placeholder'
    WIDTH_100 = 'width: 100%;'
    WIDTH_90 = 'width: 90%;'


# Task model fields
class TaskFields:
    TASK_ID = 'task_id'
    ID = 'id'
    PID = 'pid'
    ASSIGNED_TO = 'assigned_to'
    ASSIGNED_BY = 'assigned_by'
    TASK_TITLE = 'task_title'
    TITLE_TEXT = 'Increase milkability to {}%'
    TASK_DESCRIPTION = 'task_description'
    CURRENT_READABILITY = 'current_readability'
    TARGET_READABILITY = 'target_readability'
    DUE_DATE = 'due_date'
    CREATED_DATE = 'created_date'
    PROGRESS = 'progress'
    SUBSTATION = 'substation'
    UPDATE_FIELDS = 'update_fields'


class ReportsFields:
    MIN_MAX_DATES_OF_DATE_DROPDOWN = {'min': '2000-12-12',
                                      'max': datetime.now().strftime('%Y.%m.%d').replace('.', '-'),
                                      'class': 'dropbtn',
                                      'style': Style.SELECT_STYLE
                                      }
    FARM_NAME = 'Farm name'
    ID = 'Id'
    WORKSHEET_NAME = "Report table"
    RESULT = 'Result'
    AVERAGE = 'Average'
    CONTENT_DISPOSITION = 'Content-Disposition'
    CONTENT_TYPE = 'application/vnd.ms-excel'
    ATTACHMENT = "attachment; filename=Report.xlsx"
    CSS_FOR_DROPDOWN = 'dropbtn'
    UPLOAD_OBJECTS_FOR_SELECTION = 'upload_objects_for_selection'
    REPORT_EXPORT ='export'


class AuditTrailConstants:
    USER = 'user'
    REQUEST = 'request'
    GET_RESPONSE = 'get_response'
    EVENT_TITLE = "event_title"
    EVENT_DESCRIPTION = "event_description"
    EVENT_DATE = "event_date"
    RESPONSE = 'response'
    CREATED_TASK = 'Created task'
    NEW_TASK_CREATED = 'New task created'
    CREATED_SUBTASK = 'Created subtask'
    NEW_SUBTASK_CREATED = "Created subtask, pid is {}"
    UPDATED_TASK = 'Updated task'
    UPDATED_TASK_INFO = 'Updated task id is {}, progress became {}'
    USER_LOGIN = 'User login'
    USER_LOGOUT = 'User logout'
    LOGIN_FAILED = 'Login failed'
    USER_DOES_NOT_EXIST = 'User with entered email does not exist'
    WRONG_PASSWORD = 'Entered wrong password'
    CREATED_NEW_USER = 'Created new user'
    UPDATED_USER = "Updated user's data"
    CREATED_USER_INFO = "Created user {} {}"
    UPDATED_USER_INFO = "Updated  {} {}'s data"


class Errors:
    CONVERSION_ERROR = 'date_error'
    CONVERSION_ERROR_MESSAGE = 'Start date must be less then end date.'
    OUT_OF_RANGE_ERROR_MESSAGE = 'No data in selected range of days'
    OUT_OF_RANGE_ERROR = 'out_of_range'


class Fields:
    FIELDS = 'fields'
    NAME = 'name'
    PERMISSIONS = 'permissions'


class UserRoles:
    ADMIN = 'Admin'
    ANALYST = "Analyst"
    TASK_CREATOR = 'Task creator'
    TASK_DISTRIBUTOR = 'Task distributor'
    TASK_EXECUTOR = 'Task executor'

    GROUP_NAMES = (ADMIN, ANALYST, TASK_CREATOR, TASK_EXECUTOR, TASK_DISTRIBUTOR)


class ServiceLocationsConstants:
    YEREVAN = 'Yerevan'
    GYUMRI = 'Gyumri'
    VANADZOR = 'Vanadzor'
    GORIS = 'Goris'
    ARTASHAT = 'Artashat'
    STEPANAVAN = 'Stepanavan'

    SERVICE_LOCATIONS = (YEREVAN, GYUMRI, VANADZOR, GORIS, ARTASHAT, STEPANAVAN)


class Progress:
    NEW = 'New'
    IN_PROGRESS = 'In progress'
    REJECTED = 'Rejected'
    COMPLETED = 'Completed'

    PROGRESS = (NEW, IN_PROGRESS, REJECTED, COMPLETED)


FERNET = Fernet(b'neje8M9_zv2p3wI5dgLN-7jf_nMcqPytMh5GPsMBzFI=')
