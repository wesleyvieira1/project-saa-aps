from django.shortcuts import render
from .models import Disciplina
from .forms import disciplinaForm
from django.views.generic import ListView, CreateView

class disciplinaCreateView(CreateView):
    model = Disciplina
    form_class = disciplinaForm
    success_url = '/disciplinas/'
    success_message = 'Cadastrado com sucesso'

    def get_success_message(self, cleaned_data):
        return self.success_message 

class listagemDisciplinaView(ListView):
    model = Disciplina
    queryset = Disciplina.objects.all().order_by('nome_disciplina')
    

