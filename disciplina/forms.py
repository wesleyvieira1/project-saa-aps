from django import forms
from .models import Disciplina

class disciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome_disciplina','nome_professor']