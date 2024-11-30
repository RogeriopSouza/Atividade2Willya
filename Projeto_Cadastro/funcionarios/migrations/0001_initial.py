# Generated by Django 5.1.3 on 2024-11-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('cargo', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
    ]
