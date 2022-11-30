from django.shortcuts import render
from .models import Turma
from .forms import turmaForm
from django.views.generic import ListView, CreateView
from braces.views import GroupRequiredMixin

class turmaCreateView(GroupRequiredMixin,CreateView):
    group_required = [u'coord',u'professor']
    model = Turma
    form_class = turmaForm
    success_url = '/turmas/'
    success_message = 'Cadastrado com sucesso'

    def get_success_message(self, cleaned_data):
        return self.success_message 

class listagemTurmaView(GroupRequiredMixin,ListView):
    group_required = [u'coord',u'professor']
    model = Turma
    queryset = Turma.objects.all().order_by('ano_turma')