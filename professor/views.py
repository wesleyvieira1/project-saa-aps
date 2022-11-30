from django.shortcuts import render
from .models import Professor
from django.views.generic import ListView, CreateView
from .forms import professorForm
from braces.views import GroupRequiredMixin

class listagemProfessorView(GroupRequiredMixin,ListView):
    group_required = [u'coord',u'professor']
    model = Professor
    queryset = Professor.objects.all().order_by('nome_professor')

class professorCreateView(GroupRequiredMixin,CreateView):
    group_required = [u'coord',u'professor']
    model = Professor
    form_class = professorForm
    success_url = '/professores/'
    success_message = "Cadastrado com sucesso"


    def get_success_message(self, cleaned_data):
        return self.success_message 
