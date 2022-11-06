from unicodedata import name
from django.urls import path
from .views import listagemProfessorView, professorCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(listagemProfessorView.as_view()), name='professor.index'),
    path('novo/', login_required(professorCreateView.as_view()), name='professor.novo'),
]