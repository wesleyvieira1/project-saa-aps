from django.db import models
from base.validators import validateContato, validateCpf, validateDigits, validateEmail, validateEndereco, validateFoto, validateHistorico, validateNoDigits, validateNome, validateRg, validateSenha

# Create your models here.

class Usuario(models.Model):
    choices_usuario_departamento = (
        ('1','Coordenação'),
        ('2','Professor'),
        ('3','Aluno')
    )

    choices_usuario_turno = (
        ('1','Manhã'),
        ('2', 'Tarde'),
        ('3','Integral')
    )

    nome = models.CharField(max_length=100, blank=False, null=True, validators=[validateNome,validateNoDigits])
    email = models.CharField(max_length=100, blank=False, null=True, unique=True, validators=[validateEmail])
    contato = models.CharField(max_length=11, blank=False, null=True, validators=[validateContato])
    cpf = models.CharField(max_length=11, blank=False, null=True, unique=True, validators=[validateCpf])
    rg = models.CharField(max_length=7, blank=False, null=True, unique=True, validators=[validateRg])
    endereco = models.CharField(max_length=100, blank=False, null=True, validators=[validateEndereco])
    data_nascimento = models.DateField()
    data_entrada = models.DateField()
    turno = models.CharField(max_length=10, blank=False, null=True, choices=choices_usuario_turno)
    departamento = models.CharField(max_length=10, blank=False, null=True, choices=choices_usuario_departamento)


    def __str__(self):
        return self.nome