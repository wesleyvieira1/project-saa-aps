from django.urls import path
from .views import listagemDisciplinaView, disciplinaCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(listagemDisciplinaView.as_view()), name='disciplina.index'),
    path('novo/', login_required(disciplinaCreateView.as_view()), name='disciplina.novo'),
]