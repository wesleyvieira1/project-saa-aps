from django.urls import path
from .views import listagemTurmaView, turmaCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(listagemTurmaView.as_view()), name='turma.index'),
    path('novo/', login_required(turmaCreateView.as_view()), name='turma.novo')

]