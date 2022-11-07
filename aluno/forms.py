from django import forms
from .models import Aluno
class alunoForm(forms.ModelForm):
    historico = forms.FileField(label='Histórico', required=False)
    class Meta:
        model = Aluno
        fields = ['nome_aluno','historico']