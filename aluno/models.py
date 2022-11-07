from django.db import models
from usuario.models import Usuario

class Aluno(models.Model):
    nome_aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'departamento': 'Aluno'})


    def __str__(self) -> str:
        return str(self.nome_aluno)