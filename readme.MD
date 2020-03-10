# FOREX DATA ETL
This is a ETL project for Foriegn Exchange Data from twenty-two countries for the period of 2000-present.

## Pre-requisites

  1. Python
  2. Pandas
  3. psycopy2
  4. django
  5. postgresql
  
## Details
  All the details regarding the project can be found here:


docs/ForexData_Word.docx
  
## Django 

python3 manage.py runserver

It opens the Django in its default port:

Django Admin Super User:
User: gtuser
Password: rpython

## "postgresql" used in this project is from Google Cloud and the access is restricted from GeorgiaTech IP only.




## For Public Access Please update the settings.py for postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', * postgresql
        'NAME': 'databasename',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'hostname  or ip',
        'PORT': 'port',
    }
}

## Django Instructions
1. Clone the repository URL https://github.com/ishanku/ForexDataAnalysis
3. Go to the Folder "ForexDataAnalysis"
4. conda activate "<your virtual environment name>"
5. conda install django

## To Create Models after updating settings.py
1. python3 manage.py makemigrations
2. python3 manage.py migrate
3. python3 manage.py runserver

This will launch Django in the port number 8000 visit http://localhost:8000




