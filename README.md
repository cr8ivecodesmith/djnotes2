djnotes2
========

## Hello Django

### 01) Install Django and run it for the first time

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


### 02) Create a super user and visit the admin page

```
hello_django > python manage.py createsuperuser
hello_django > python manage.py runserver
```

Open browser to: http://127.0.0.1:8000/admin

```
<CTRL>+C (to stop the server)
```


### 03) Create a `home` app

```
hello_django > python manage.py startapp home
```


### 04) Create the home view, template, and url

Edit:
```
hello_django/home/views.py
```

```python
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'
```


Edit:
```
hello_django/hello_django/settings.py
```

```python
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home',
]
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...
```

```
hello_django > mkdir -p templates/home
hello_django > touch templates/home/index.html
```


Create the template file:
```
hello_django/templates/home/index.html
```

```html
<!DOCTYPE html>
<html lang="en-us">
<head>
    <title>The Hello Django App</title>
</head>
<body>
    <h1>Hello Django!</h1>
</body>
</html>
```


Create the URL route and check your new home page:
```
hello_django/hello_django/urls.py
```

```python
...
from home import views as home_views

urlpatterns = [
    url(r'^$', home_views.Index.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
]
```

```
hello_django > python manage.py runserver
```

Open browser to: http://127.0.0.1:8000
