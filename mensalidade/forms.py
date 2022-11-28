from django import forms
from .models import Mensalidade

class mensalidadeForm(forms.ModelForm):
    data_pagamento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    class Meta:
        model = Mensalidade
        fields =  ['nome_aluno','valor','data_pagamento','forma_pagamento']