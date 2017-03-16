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


## Notes App

### 01) Start a new Django project and create the initial scaffolds

```
> django-admin startproject notes_app
> cd notes_app
notes_app > mkdir -p templates/notes
notes_app > touch templates/base.html
notes_app > touch templates/notes/list.html
notes_app > touch templates/notes/view.html
notes_app > touch templates/notes/create.html
notes_app > touch templates/notes/update.html
notes_app > touch templates/notes/delete.html
notes_app > mkdir assets
notes_app > touch assets/scripts.js
notes_app > touch assets/styles.css
notes_app > python manage.py startproject notes
```


### 02) Update the settings file

Edit:
```
notes_app/notes_app/settings.py
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

    'notes',
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
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]
```


### 03) Define and create the Note model

Edit:
```
notes_app/notes/models.py
```

```python
...
class Note(models.Model):
    title = models.CharField(max_length=1024, blank=True)
    note = models.TextField(blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

```
notes_app > python manage.py makemigrations
notes_app > python manage.py migrate
```


### 04) Create the note list view, template, and url route

Edit:
```
notes_app/notes/views.py
```

```python
```


Edit:
```
notes_app/templates/base.html
```

```html

```


Edit:
```
notes_app/templates/notes/list.html
```

```html
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
```


### 05) Create the note create view, template, and url route

Edit:
```
notes_app/notes/views.py
```


Edit:
```
notes_app/templates/notes/create.html
```

```html
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
```


### 06) Create the note update view, template, and url route

Edit:
```
notes_app/notes/views.py
```


Edit:
```
notes_app/templates/notes/update.html
```

```html
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
```


### 07) Create the note delete view, template, and url route

Edit:
```
notes_app/notes/views.py
```


Edit:
```
notes_app/templates/notes/delete.html
```

```html
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
```
