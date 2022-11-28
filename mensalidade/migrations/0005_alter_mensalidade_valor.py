# Generated by Django 4.1.3 on 2022-11-10 12:07

import base.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensalidade', '0004_mensalidade_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensalidade',
            name='valor',
            field=models.CharField(max_length=50, null=True, validators=[base.validators.validateDigits]),
        ),
    ]