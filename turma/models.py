from django.db import models
from professor.models import Professor
from aluno.models import Aluno
from disciplina.models import Disciplina

# Create your models here.
class Turma(models.Model):

    ano_turma_choices = (
        ('1A','1º ano - Fundamental I'),
        ('2A','2º ano - Fundamental I'),
        ('3A','3º ano - Fundamental I'),
        ('4A','4º ano - Fundamental I'),
        ('5A','5º ano - Fundamental I'),
        ('6A','6º ano - Fundamental II'),
        ('7A','7º ano - Fundamental II'),
        ('8A','8º ano - Fundamental II'),
        ('9A','9º ano - Fundamental II'),
        ('1EM','1º ano - Ensino Médio'),
        ('2EM','2º ano - Ensino Médio'),
        ('3EM','3º ano - Ensino Médio'),
    )

    ano_turma = models.CharField(max_length=50, choices=ano_turma_choices)
    nome_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nome_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return str(self.nome_professor),str(self.nome_disciplina),str(self.nome_aluno)