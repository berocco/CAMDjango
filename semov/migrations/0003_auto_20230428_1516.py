# Generated by Django 3.2.16 on 2023-04-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semov', '0002_inscricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='capas')),
                ('ano', models.IntegerField()),
                ('dias', models.IntegerField()),
                ('empresas', models.IntegerField()),
                ('eventos', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='inscricao',
            options={'verbose_name': 'Inscrição', 'verbose_name_plural': 'Inscrições'},
        ),
    ]