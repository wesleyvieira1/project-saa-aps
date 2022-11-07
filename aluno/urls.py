from unicodedata import name
from django.urls import path
from .views import listagemAlunoView, alunoCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(listagemAlunoView.as_view()), name='aluno.index'),
    path('novo/', login_required(alunoCreateView.as_view()), name='aluno.novo'),
]