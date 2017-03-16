"""notes_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from notes import views as notes_views

urlpatterns = [
    url(r'^$', notes_views.NoteList.as_view(), name='note_list'),
    url(r'^create/$', notes_views.NoteCreate.as_view(), name='note_create'),
    url(r'^(?P<pk>\d+)/change/$', notes_views.NoteUpdate.as_view(), name='note_update'),
    url(r'^admin/', admin.site.urls),
]
