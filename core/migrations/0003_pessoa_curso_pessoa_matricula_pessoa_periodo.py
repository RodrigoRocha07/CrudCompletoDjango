# Generated by Django 4.2.2 on 2023-07-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pessoa_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='curso',
            field=models.CharField(default='Vazio', max_length=100),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='matricula',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='periodo',
            field=models.CharField(default='Primeiro', max_length=100),
        ),
    ]
