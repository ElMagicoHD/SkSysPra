from django.db import models

class ToDo(models.Model):
    content = models.CharField(max_length=160)
    progress = models.IntegerField()
    due_date = models.DateField()