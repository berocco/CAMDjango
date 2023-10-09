# Generated by Django 3.2.16 on 2023-05-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('inscricao', models.CharField(max_length=100)),
                ('tags', models.ManyToManyField(blank=True, to='estagios.Tag')),
            ],
        ),
    ]