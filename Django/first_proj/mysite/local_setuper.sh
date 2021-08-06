#!/bin/bash 

main () {
	#Start the Postgres     
	systemctl status postgresql     
	systemctl start postgresql      

	#Virtualenc modules installation
	source venv/bin/activate

	#Create tables
	python manage.py makemigrations
	python manage.py migrate

	#Start the application
	python manage.py runserver
}

main

