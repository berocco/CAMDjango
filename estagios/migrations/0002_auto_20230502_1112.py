# Generated by Django 3.2.16 on 2023-05-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaga',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição da vaga'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='inscricao',
            field=models.CharField(max_length=100, verbose_name='Inscrição'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
