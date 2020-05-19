from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=160)
    progress = models.IntegerField()
    due_date = models.DateField()
    