from django.db import models
from professor.models import Professor

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=50, blank=False, null=True)
    nome_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    ano = models.DateField()

    def __str__(self) -> str:
        return str(self.nome_disciplina)
