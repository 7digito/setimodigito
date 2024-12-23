# Generated by Django 4.2.16 on 2024-10-22 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('extensao', models.CharField(choices=[('.com', '.com'), ('.pt', '.pt'), ('.net', '.net'), ('.org', '.org'), ('.bizz', '.bizz')], max_length=10)),
                ('estado', models.CharField(choices=[('ativo', 'Ativo'), ('suspenso', 'Suspenso'), ('expirado', 'Expirado'), ('terminado', 'Terminado')], max_length=10)),
                ('data_criacao', models.DateTimeField()),
                ('data_expiracao', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dominios', to='clientes.cliente')),
            ],
        ),
    ]
