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
