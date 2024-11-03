# Generated by Django 5.1.2 on 2024-11-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalhos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposta',
            name='data_entrega',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proposta',
            name='data_expiracao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proposta',
            name='validade_em_dias',
            field=models.PositiveIntegerField(default=30),
        ),
    ]