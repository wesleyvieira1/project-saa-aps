from django.shortcuts import render
from .models import RegistroAula
from .forms import registroForm
from django.views.generic import ListView, CreateView
from braces.views import GroupRequiredMixin

class registroView(GroupRequiredMixin,CreateView):
    group_required = [u'coord',u'professor']
    model = RegistroAula
    form_class = registroForm
    success_url = '/turmas/'
    success_message = 'Cadastrado com sucesso'

    def get_success_message(self, cleaned_data):
        return self.success_message 

class listagemRegistroView(GroupRequiredMixin,ListView):
    group_required = [u'coord',u'professor']
    model = RegistroAula
    queryset = RegistroAula.objects.all().order_by('data_aula')