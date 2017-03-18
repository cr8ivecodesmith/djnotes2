djnotes2
========

Feedback: https://goo.gl/forms/utNMS1ypBe2s9H892
Presenter entry: https://goo.gl/forms/88HUlZ5bmVa2QTUg2

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
notes_app > python manage.py startapp notes
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
from django.shortcuts import render
from django.views.generic import View

from .models import Note


class NoteList(View):
    template_name = 'notes/list.html'

    def get_context_data(self):
        context = {}
        context['note_list'] = Note.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
```


Edit:
```
notes_app/templates/base.html
```

```html
{% load static %}
<!DOCTYPE html>
<html lang="en-us">
<head>
    <title>Simple Notes</title>

    <!-- Custom styles -->
    <link rel="stylesheet" type="text/css"
        href="{% static 'styles.css' %}">
</head>
<body>
    {% block content %}
    {% endblock content %}

    <!-- Custom scripts -->
    <script src="{% static 'scripts.js' %}">
    </script>
</body>
</html>
```


Edit:
```
notes_app/templates/notes/list.html
```

```html
{% extends 'base.html' %}

{% block content %}
<h1>Notes</h1>
<hr>

<ol>
{% for note in note_list %}
<li><a href="#">{{ note.title|default:note.id }}</a></li>
{% endfor %}
</ol>

{% endblock content %}
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
...
from notes import views as notes_views

urlpatterns = [
    url(r'^$', notes_views.NoteList.as_view(), name='note_list'),
    url(r'^admin/', admin.site.urls),
]
```


### 05) Create the note create view, template, and url route

Edit:
```
notes_app/notes/views.py
```

```python
class NoteCreate(View):
    template_name = 'notes/create.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        title = request.POST.get('txtTitle', '')
        note = request.POST.get('txtNote', '')
        if title or note:
            Note.objects.create(
                title=title,
                note=note
            )
        return redirect('note_list')
```


Edit:
```
notes_app/templates/notes/create.html
```

```html
{% extends 'base.html' %}

{% block content %}
<h1>Create Note</h1>
<hr>

<form action="" method="post">
    {% csrf_token %}
    <input type="text"
        name="txtTitle" placeholder="Enter title...">
    <br>
    <textarea
        name="txtNote" rows="10em"
        placeholder="Enter note..."></textarea>
    <br>
    <input type="submit" value="Save">
    <a href="{% url 'note_list' %}">Cancel</a>
</form>
{% endblock content %}
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
...
    url(r'^$', notes_views.NoteList.as_view(), name='note_list'),
    url(r'^create/', notes_views.NoteCreate.as_view(), name='note_create'),
...
```


Edit:
```
notes_app/templates/notes/list.html
```

```html
...
<h1>Notes</h1>
<hr>
<a href="{% url 'note_create' %}">New note</a>
...
```


### 06) Create the note update view, template, and url route

Edit:
```
notes_app/notes/views.py
```

```python
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
...
class NoteUpdate(View):
    template_name = 'notes/update.html'

    def get_context_data(self, **kwargs):
        context = {}
        try:
            note_id = kwargs.get('pk')
            note = Note.objects.get(id=note_id)
            context['note'] = note
        except Note.DoesNotExist:
            raise Http404
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        note = context.get('note')
        note_title = request.POST.get('txtTitle', '').strip()
        note_note = request.POST.get('txtNote', '').strip()
        note.title = note_title
        note.note = note_note
        note.save()
        return render(request, self.template_name, context)
```


Edit:
```
notes_app/templates/notes/update.html
```

```html
{% extends 'base.html' %}

{% block content %}
<h1>Update Note {{ note.id }}</h1>
<hr>

<form action="{% url 'note_update' note.id %}" method="post">
    {% csrf_token %}
    <input type="text"
        name="txtTitle" value="{{ note.title }}" placeholder="Enter title...">
    <br>
    <textarea
        name="txtNote" rows="10em"
        placeholder="Enter note...">{{ note.note }}</textarea>
    <br>
    <input type="submit" value="Save">
    <a href="{% url 'note_list' %}">Cancel</a>
</form>
{% endblock content %}
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
...
    url(r'^create/$', notes_views.NoteCreate.as_view(), name='note_create'),
    url(r'^(?P<pk>\d+)/change/$', notes_views.NoteUpdate.as_view(), name='note_update'),
...
```


Edit:
```
notes_app/templates/notes/list.html
```

```html
...
{% for note in note_list %}
<li><a href="{% url 'note_update' note.id %}">{{ note.title|default:note.id }}</a></li>
{% endfor %}
...
```

### 07) Create the note delete view, template, and url route

Edit:
```
notes_app/notes/views.py
```

```python
...
class NoteDelete(NoteUpdate):
    template_name = 'notes/delete.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        note = context.get('note')
        note.delete()
        return redirect('note_list')
...
```


Edit:
```
notes_app/templates/notes/delete.html
```

```html
{% extends 'base.html' %}

{% block content %}
<h1>Delete Note {{ note.id }}?</h1>
<hr>

<form action="{% url 'note_delete' note.id %}" method="post">
    {% csrf_token %}
    <input type="text"
        name="txtTitle" value="{{ note.title }}" placeholder="Enter title...">
    <br>
    <textarea
        name="txtNote" rows="10em"
        placeholder="Enter note...">{{ note.note }}</textarea>
    <br>
    <input type="submit" value="Delete">
    <a href="{% url 'note_update' note.id %}">Cancel</a>
</form>
{% endblock content %}
```


Edit:
```
notes_app/notes_app/urls.py
```

```python
...
    url(r'^(?P<pk>\d+)/change/$', notes_views.NoteUpdate.as_view(), name='note_update'),
    url(r'^(?P<pk>\d+)/delete/$', notes_views.NoteDelete.as_view(), name='note_delete'),
...
```


Edit:
```
notes_app/templates/notes/update.html
```

```html
...
    <input type="submit" value="Save">
    <a href="{% url 'note_delete' note.id %}">Delete</a>
    <a href="{% url 'note_list' %}">Cancel</a>
...
```
