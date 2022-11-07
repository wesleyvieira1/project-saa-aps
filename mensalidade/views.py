from django.shortcuts import render
from .models import Mensalidade
from django.views.generic import ListView, CreateView
from .forms import mensalidadeForm

class listagemMensalidadeView(ListView):
    model = Mensalidade
    queryset = Mensalidade.objects.all().order_by('nome_aluno')

class mensalidadeCreateView(CreateView):
    model = Mensalidade
    form_class = mensalidadeForm
    success_url = '/mensalidades/'
    success_message = "Cadastrado com sucesso"


    def get_success_message(self, cleaned_data):
        return self.success_message 
