djnotes2
========

## Hello Django

### Install Django and run it for the first time

```
> pip install django
> django-admin startproject hello_django
> cd hello_django
hello_django > python manage.py migrate
hello_django > python manage.py runserver
```

Open browser to: http://127.0.0.1:8000

```
<CTRL>+C (to stop the server)
```


### Create a super user and visit the admin page

```
hello_django > python manage.py createsuperuser
hello_django > python manage.py runserver
```

Open browser to: http://127.0.0.1:8000/admin

```
<CTRL>+C (to stop the server)
```


### Create a `home` app

```
hello_django > python manage.py startapp home
```
