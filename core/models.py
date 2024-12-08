from django.db import models


class Task(models.Model):
    
    descricao = models.CharField( max_length=50,  null=False)
    completo = models.BooleanField(default=False, null=False)
    
    
    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

