# Generated by Django 5.1.2 on 2024-10-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dominios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dominio',
            name='data_expiracao',
            field=models.DateTimeField(),
        ),
    ]
