from unicodedata import name
from django.urls import path
from .views import listagemMensalidadeView, mensalidadeCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(listagemMensalidadeView.as_view()), name='mensalidade.index'),
    path('novo/', login_required(mensalidadeCreateView.as_view()), name='mensalidade.novo'),
]