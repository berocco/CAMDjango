# Generated by Django 3.2.16 on 2023-04-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticpages', '0006_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField(max_length=511)),
                ('imagem', models.ImageField(upload_to='slides')),
                ('link', models.URLField(max_length=100)),
                ('ordem', models.IntegerField()),
            ],
        ),
    ]
