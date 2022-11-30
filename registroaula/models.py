from django.db import models
from professor.models import Professor

class RegistroAula(models.Model):
    data_aula = models.DateField()
    num_aulas = models.IntegerField()
    descricao = models.TextField(max_length=200)
    nome_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.nome_professor)