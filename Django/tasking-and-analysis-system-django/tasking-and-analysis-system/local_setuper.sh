#!/bin/bash 

main () {
    #Start the Postgres	
    systemctl status postgresql	
    systemctl start postgresql	

    #Virtualenc modules installation
    source venv/bin/activate
    pip install -r requirements.txt

    #Create tables
    python manage.py makemigrations
    python manage.py migrate

    #Create users, roles ...
    python manage.py create_roles
    python manage.py create_progresses
    python manage.py create_service_locations
    python manage.py create_admin
    python manage.py create_users

    #Start the application
    #python manage.py runserver
}

main
