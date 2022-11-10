from django.db import models
from aluno.models import Aluno
#from base.validators import validateDate

class Mensalidade(models.Model):
    pagamento_choices=(
        ('cartão de crédito','cartão de crédito'),
        ('cartão de déito','cartão de débito'),
        ('pix','pix'),
        ('dinheiro','dinheiro')
    )

    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    forma_pagamento = models.CharField(max_length=50, blank=False, null=True, choices=pagamento_choices)

    def __str__(self) -> str:
        return self.nome_aluno