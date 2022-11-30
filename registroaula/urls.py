from django.urls import path
from .views import registroView, listagemRegistroView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('novo-registro/', login_required(registroView.as_view()), name='registro.novo'),
    path('registros/', login_required(listagemRegistroView.as_view()), name='registro.index')
]