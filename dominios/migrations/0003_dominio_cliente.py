# Generated by Django 5.1.2 on 2024-10-21 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('dominios', '0002_alter_dominio_data_expiracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='dominio',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dominios', to='clientes.cliente'),
            preserve_default=False,
        ),
    ]