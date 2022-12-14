# Generated by Django 4.1.2 on 2022-10-28 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=20)),
                ('data_nasc', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia', models.CharField(max_length=10)),
                ('conta', models.CharField(max_length=6)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
                ('ultima_movimentacao', models.DateTimeField(auto_now=True)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loteria.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Sorteio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('numeros', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Saque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave_pix', models.CharField(max_length=80)),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('data_deposito', models.DateTimeField(auto_now_add=True)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loteria.contas')),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('numeros', models.CharField(max_length=120)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loteria.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('data_deposito', models.DateTimeField(auto_now_add=True)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loteria.contas')),
            ],
        ),
    ]
