from django.shortcuts import render
from .models import Aluno
from django.views.generic import ListView, CreateView
from .forms import alunoForm

class listagemAlunoView(ListView):
    model = Aluno
    queryset = Aluno.objects.all().order_by('nome_aluno')

class alunoCreateView(CreateView):
    model = Aluno
    form_class = alunoForm
    success_url = '/alunos/'
    success_message = "Cadastrado com sucesso"

    def get_success_message(self, cleaned_data):
        return self.success_message 