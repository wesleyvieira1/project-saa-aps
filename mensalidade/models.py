from django.db import models
from aluno.models import Aluno
from base.validators import validateDigits

class Mensalidade(models.Model):
    pagamento_choices=(
        ('cartão de crédito','cartão de crédito'),
        ('cartão de déito','cartão de débito'),
        ('pix','pix'),
        ('dinheiro','dinheiro')
    )
    meses_choices = (
        ('jan','Janeiro'),
        ('fev','Fevereiro'),
        ('mar','Março'),
        ('abr','Abril'),
        ('mai','Maio'),
        ('jun','Junho'),
        ('jul','Julho'),
        ('ago','Agosto'),
        ('set','Setembro'),
        ('out','Outubro'),
        ('nov','Novembro'),
        ('dez','Dezembro')
    )

    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    valor = models.CharField(max_length=50, blank=False, null=True, validators=[validateDigits])
    forma_pagamento = models.CharField(max_length=50, blank=False, null=True, choices=pagamento_choices)
    mes_referente = models.CharField(max_length=50, blank=False, null=True, choices=meses_choices)

    def __str__(self) -> str:
        return self.nome_aluno