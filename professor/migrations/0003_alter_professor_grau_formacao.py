# Generated by Django 4.1.3 on 2022-11-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_alter_professor_nome_professor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='grau_formacao',
            field=models.CharField(choices=[('Graduado', 'Graduado'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado')], max_length=10, null=True),
        ),
    ]
