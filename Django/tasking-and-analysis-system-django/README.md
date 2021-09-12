# Tasking and Analysis System
The system is designed to upload data, create tasks, track their life cycle and generate reports about uploaded data.


> Features
- PostgreSQL Database, Django ORM


> Links

- [Tasking and Analysis System](https://www.figma.com/file/zqhAzlkeUEk5rTtuCQtNjS/ITC?node-id=4%3A10) - product design
- [Tasking and Analysis System](https://gitlab.com/im-itc/tasking-and-analysis-system-django/-/tree/develop/docs) - product documentation 


# HOW TO RUN PROGRAM (on linux)
## Installation
At first open terminal and enter commands below.
```bash
git clone https://gitlab.com/im-itc/tasking-and-analysis-system-django.git
cd tasking-and-analysis-system-django/tasking-and-analysis-system-django
```
Then we need to install and create virtual environment.
```bash
sudo apt install virtualenv
virtualenv venv
source venv/bin/activate
```
Then download postgresql (see [https://www.postgresql.org/download/linux/ubuntu/](https://www.postgresql.org/download/linux/ubuntu/))
Enter postgres.
```bash
sudo -u postgres psql
```
Create user and database
```bash
create user tas_itc with encrypted password 'tas_itc';
create database tas_itc;
grant all privileges on database tas_itc to tas_itc;
```
Then type ctrl + D
Now we need to
-install requirements
-create tables in database
-create roles, users(for each role)
-create service locations and progresses
For that we need to run following script
```bash
source local_setuper.sh
```
## Usage
Run the program with following command
```bash
python manage.py runserver
```
Access the web app in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
---
If you want to enter the system as:
---
__ADMIN:__

__login:__ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; admin@gmail.com

__password:__ &nbsp; admin

__ANALYST:__

__login:__ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; analyst@yopmail.com

__password:__ &nbsp; admin

__TASK CREATOR:__

__login:__ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; task_creator@yopmail.com

__password:__ &nbsp; admin

__TASK DISTRIBUTOR:__

__login:__ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; task_distributor@yopmail.com

__password:__ &nbsp; admin

__TASK EXECUTOR:__

__login:__ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; task_executor@yopmail.com

__password:__ &nbsp; admin

<br />

## Code-base structure

The project is coded using a simple and intuitive structure presented bellow:
```bash
< PROJECT ROOT >
├── apps
│   ├── audit_trail
│   │   ├── admin.py
│   │   ├── configs.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── authentication
│   │   ├── admin.py
│   │   ├── config.py
│   │   ├── email_backend.py
│   │   ├── forms.py
│   │   ├── helper.py
│   │   ├── management
│   │   │   └── commands
│   │   │       ├── create_admin.py
│   │   │       ├── create_progresses.py
│   │   │       ├── create_roles.py
│   │   │       ├── create_service_locations.py
│   │   │       └── create_users.py
│   │   ├── managers.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── user_permissions.py
│   │   ├── validators
│   │   │   └── CustomPasswordValidator.py
│   │   └── views.py
│   ├── constants.py
│   ├── dashboard
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── helper.py
│   │   ├── manager.py
│   │   ├── models.py
│   │   ├── templatetags
│   │   │   └── previous_element_tag.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manager.py
│   ├── reports
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── helper.py
│   │   ├── manager.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── tasks
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── helper.py
│   │   ├── manager.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── upload
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── helper.py
│       ├── manager.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── core
│   ├── asgi.py
│   ├── settings.py
│   ├── static
│   │   └── assets
│   │       ├── css
│   │       ├── fonts
│   │       ├── img
│   │       ├── js
│   │       └── sass
│   ├── templates
│   │   ├── accounts
│   │   │   ├── confirm_password.html
│   │   │   ├── login.html
│   │   │   └── password
│   │   │       ├── invitation_email.html
│   │   │       └── password_reset_email.html
│   │   ├── admin
│   │   │   └── app_list.html
│   │   ├── includes
│   │   │   ├── configuration-plugin.html
│   │   │   ├── footer.html
│   │   │   ├── navigation.html
│   │   │   ├── scripts.html
│   │   │   └── sidebar.html
│   │   ├── layouts
│   │   │   ├── base-fullscreen.html
│   │   │   └── base.html
│   │   └── main_templates
│   │       ├── audit
│   │       │   └── audit_trail.html
│   │       ├── index.html
│   │       ├── reports
│   │       │   └── report.html
│   │       ├── tasks
│   │       │   ├── task_create_or_edit.html
│   │       │   └── task_index.html
│   │       ├── upload
│   │       │   └── upload.html
│   │       └── view_more.html
│   ├── urls.py
│   └── wsgi.py
├── local_setuper.sh
├── manage.py
└── requirements.txt

30 directories, 89 files
