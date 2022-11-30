from django import forms
from .models import RegistroAula


class registroForm(forms.ModelForm):
    data_aula = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = RegistroAula
        fields = '__all__'