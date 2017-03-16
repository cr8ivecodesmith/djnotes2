from django.shortcuts import render, redirect
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
