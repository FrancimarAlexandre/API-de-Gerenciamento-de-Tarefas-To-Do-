from django.db import models

# Create your models here.


class Tarefa(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return f"Tarefa {self.title}"
