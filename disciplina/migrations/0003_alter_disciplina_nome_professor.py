# Generated by Django 4.1.3 on 2022-11-06 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
        ('disciplina', '0002_remove_disciplina_nome_professor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='nome_professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor.professor'),
        ),
    ]