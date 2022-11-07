from django.db import models
from usuario.models import Usuario
# Create your models here.
class Professor(models.Model):
    choices_grau= (
        ('Graduado','Graduado'),
        ('Mestrado','Mestrado'),
        ('Doutorado','Doutorado'),
    )
    nome_professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'departamento': 'Professsor'})
    grau_formacao = models.CharField(max_length=10, blank=False, null=True, choices=choices_grau)
    formacao = models.CharField(max_length=20, blank=False, null=True)

    def __str__(self) -> str:
        return str(self.nome_professor)