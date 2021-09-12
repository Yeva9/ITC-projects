class Permissions:
    CAN_VIEW_ADMIN_PAGE = (
        "can_view_admin_page",
        "Can view admin page"
    )

    CAN_VIEW_UPLOAD_PAGE = (
        "can_view_upload_page",
        "Can view upload page"
    )

    CAN_VIEW_TASKS_PAGE = (
        "can_view_tasks_page",
        "Can view tasks page"
    )

    CAN_VIEW_REPORTS_PAGES = (
        "can_view_reports_pages",
        "Can view reports pages"
    )

    CAN_UPLOAD_FILES_INTO_THE_SYSTEM = (
        "can_upload_files_into_the_system",
        "Can upload files into the system"
    )

    CAN_GENERATE_REPORTS = (
        "can_generate_reports",
        "Can generate reports"
    )

    CAN_EXPORT_XLSX_FILES = (
        "can_export_xlsx_files",
        "Can export xlsx files"
    )

    CAN_EXPORT_LOG_FILES = (
        "can_export_log_files",
        "Can export log files"
    )

    CAN_VIEW_TASKS_TAB = (
        "can_view_tasks_tab",
        "Can view tasks tab"
    )

    CAN_VIEW_TASK_LIST = (
        "can_view_task_list",
        "Can view task list"
    )

    CAN_VIEW_ONLY_USERS_WITH_ROLE_TASKS_DISTRIBUTOR = (
        "can_view_only_users_with_role_tasks_distributor",
        "Can view only users with role tasks distributor"
    )

    CAN_CREATE_NEW_TASK = (
        "can_create_new_task",
        "Can create new task"
    )

    CAN_ASSIGN_TASK_TO_THE_USER_WITH_TASK_DISTRIBUTOR_ROLE = (
        "can_assign_task_to_the_user_with_task_distributor_role",
        "Can assign task to the user with task distributor role"
    )

    CAN_EDIT_OWN_TASKS = (
        "can_edit_own_tasks",
        "Can edit own tasks"
    )

    CAN_ADD_USERS = (
        "can_add_users",
        "Can add users"
    )

    CAN_EDIT_USER_INFORMATION = (
        "can_edit_user_information",
        "Can edit user information"
    )

    CAN_DEACTIVATE_USERS = (
        "can_deactivate_users",
        "Can deactivate users"
    )

    CAN_DELETE_USERS = (
        "can_delete_users",
        "Can delete users"
    )

    CAN_ADD_NEW_SUBTASK = (
        "can_add_new_subtask",
        "Can add new subtask"
    )

    CAN_EDIT_OWN_SUBTASK = (
        "can_edit_own_subtask",
        "Can edit own subtask"
    )

    CAN_ASSIGN_SUBTASK_TO_USER_WITH_ROLE_TASK_EXECUTOR = (
        "can_assign_subtask_to_user_with_role_task_executor",
        "Can assign subtask to user with role task executor"
    )

    CAN_VIEW_ONLY_ASSIGNED_SUBTASKS = (
        "can_view_only_assigned_subtasks",
        "Can view only assigned subtasks"
    )

    CAN_VIEW_TASK_COUNTS_ACCORDING_TO_STATUSES = (
        "can_view_task_counts_according_to_statuses",
        "Can view task counts according to statuses"
    )

    CAN_EDIT_ASSIGNED_TASKS_ONLY_STATUS_FIELD = (
        "can_edit_assigned_tasks_only_status_field",
        "Can edit assigned tasks only status field"
    )

    def __str__(self):
        return '%s | %s' % (self.content_type, self.name)
