# Generated by Django 4.1.3 on 2022-11-29 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensalidade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensalidade',
            name='mes_referente',
            field=models.CharField(choices=[('jan', 'Janeiro'), ('fev', 'Fevereiro'), ('mar', 'Março'), ('abr', 'Abril'), ('mai', 'Maio'), ('jun', 'Junho'), ('jul', 'Julho'), ('ago', 'Agosto'), ('set', 'Setembro'), ('out', 'Outubro'), ('nov', 'Novembro'), ('dez', 'Dezembro')], max_length=50, null=True),
        ),
    ]
