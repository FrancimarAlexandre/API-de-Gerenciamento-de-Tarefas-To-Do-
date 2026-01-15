from django.db import models
from datetime import date

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_date(date):
    if date < date.today():
        raise ValidationError(
            _("%(date)s data inválida"),
            params={"date": date},
        )


class Tarefa(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    date = models.DateField(validators=[validate_date])
    created_at = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tarefas"

    def __str__(self):
        return f"Tarefa {self.title}"
