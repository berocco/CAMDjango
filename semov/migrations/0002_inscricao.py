# Generated by Django 3.2.16 on 2023-04-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semov', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('link', models.URLField(max_length=100)),
            ],
        ),
    ]