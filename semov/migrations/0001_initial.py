# Generated by Django 3.2.16 on 2023-04-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
            options={
                'verbose_name': 'Edição',
                'verbose_name_plural': 'Edições',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=31)),
                ('imagem', models.ImageField(upload_to='logos_semov')),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='patrocinadores')),
                ('link', models.URLField(max_length=100)),
            ],
        ),
    ]
