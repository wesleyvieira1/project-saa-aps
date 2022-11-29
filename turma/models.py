from django.db import models
from professor.models import Professor
from aluno.models import Aluno
from disciplina.models import Disciplina

# Create your models here.
class Turma(models.Model):
    ano_turma = models.CharField(max_length=1)
    nome_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nome_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return str(self.nome_professor),str(self.nome_disciplina),str(self.nome_aluno)