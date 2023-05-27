### Django Configuration
#### Installation
```commandline
pip install django
```
#### Project Creation
```commandline
django-admin startproject <project-name> .
```
#### Application Creation
```commandline
python manage.py startapp <app-name>
```
#### App Registration
Add the name of the application in the INSTALLED_APPS list inside settings.py.

#### Run the app
```commandline
python manage.py runserver
```

#### Stop the app
```commandline
ctrl+c
```

#### Adding tables to the database
- Add the attributes in models.py file
- Convert the models.py to database mapping file inside migrations folder using below command
    ```
    python manage.py makemigrations
    ```
- Create the tables from the database mapping file
  ```commandline
  python manage.py migrate
  ```
- Every time you wanted to update the DDL, run the above two commands.

#### Mapping the URLs to methods
- Add method to render html in views.py file
- Create urls.py to map url to views.
- Register urls.py to urls.py of project directory.

#### Configuring Django Admin
- Register the model in admin.py
- Create a superuser for Django using the below comamand
  ```commandline
  python manage.py createsuperuser
  ```
- Access the admin with /admin