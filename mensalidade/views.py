from django.shortcuts import render
from .models import Mensalidade
from django.views.generic import ListView, CreateView
from .forms import mensalidadeForm
from braces.views import GroupRequiredMixin

class listagemMensalidadeView(GroupRequiredMixin,ListView):
    group_required = [u'coord',u'aluno']
    queryset = Mensalidade.objects.all().order_by('nome_aluno')

class mensalidadeCreateView(GroupRequiredMixin,CreateView):
    group_required = [u'coord']
    model = Mensalidade
    form_class = mensalidadeForm
    success_url = '/mensalidades/'
    success_message = "Cadastrado com sucesso"


    def get_success_message(self, cleaned_data):
        return self.success_message 
