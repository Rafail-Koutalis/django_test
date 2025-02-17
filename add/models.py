from django.db import models

class Task(models.Model) :
    task_name = models.CharField(primary_key=True,max_length=20,)
    description = models.TextField(max_length=400)
    completed = models.BooleanField(default=False)
    banner = models.ImageField(default='fallback.png',blank=True) #den einai aparaititi i eikona an den tin baloyme

    def __str__(self):
        return self.task_name
  