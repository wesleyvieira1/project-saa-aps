from django import forms
from .models import Professor
class professorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome_professor', 'grau_formacao','formacao']