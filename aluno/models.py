from django.db import models
from usuario.models import Usuario
from base.validators import validateCpf

class Aluno(models.Model):
    nome_aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'departamento': 'Aluno'})
    cpf_aluno = models.CharField(max_length=11, blank=False, null=True, unique=True, validators=[validateCpf])

    def __str__(self) -> str:
        return str(self.nome_aluno)