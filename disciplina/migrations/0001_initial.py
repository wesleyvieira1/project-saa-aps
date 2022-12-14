# Generated by Django 4.1.3 on 2022-11-29 20:00

import base.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=50, null=True, validators=[base.validators.validateNoDigits])),
                ('ano', models.DateField(validators=[base.validators.validateDate])),
                ('nome_professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor.professor')),
            ],
        ),
    ]
