from django.shortcuts import render
from .models import Disciplina
from .forms import disciplinaForm
from django.views.generic import ListView, CreateView
from braces.views import GroupRequiredMixin

class disciplinaCreateView(GroupRequiredMixin,CreateView):
    group_required = [u'coord']
    model = Disciplina
    form_class = disciplinaForm
    success_url = '/disciplinas/'
    success_message = 'Cadastrado com sucesso'

    def get_success_message(self, cleaned_data):
        return self.success_message 

class listagemDisciplinaView(GroupRequiredMixin,ListView):
    group_required = [u'coord',u'professor',u'aluno']
    model = Disciplina
    queryset = Disciplina.objects.all().order_by('nome_disciplina')
    

