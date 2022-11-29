from django import forms
from .models import Turma

class turmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['ano_turma','nome_professor','nome_disciplina','nome_aluno']