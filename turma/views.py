from django.shortcuts import render
from .models import Turma
from .forms import turmaForm
from django.views.generic import ListView, CreateView

class turmaCreateView(CreateView):
    model = Turma
    form_class = turmaForm
    success_url = '/turmas/'
    success_message = 'Cadastrado com sucesso'

    def get_success_message(self, cleaned_data):
        return self.success_message 

class listagemTurmaView(ListView):
    model = Turma
    queryset = Turma.objects.all().order_by('ano_turma')
    

