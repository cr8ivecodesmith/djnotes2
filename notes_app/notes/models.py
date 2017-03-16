from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=1024, blank=True)
    note = models.TextField(blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
