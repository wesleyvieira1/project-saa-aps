# Generated by Django 4.1.3 on 2022-11-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='ano_turma',
            field=models.CharField(choices=[('1A', '1º ano - Fundamental I'), ('2A', '2º ano - Fundamental I'), ('3A', '3º ano - Fundamental I'), ('4A', '4º ano - Fundamental I'), ('5A', '5º ano - Fundamental I'), ('6A', '6º ano - Fundamental II'), ('7A', '7º ano - Fundamental II'), ('8A', '8º ano - Fundamental II'), ('9A', '9º ano - Fundamental II'), ('1EM', '1º ano - Ensino Médio'), ('2EM', '2º ano - Ensino Médio'), ('3EM', '3º ano - Ensino Médio')], max_length=50),
        ),
    ]
