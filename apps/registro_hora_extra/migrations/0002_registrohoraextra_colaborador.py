# Generated by Django 3.0.8 on 2020-07-30 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0003_auto_20200730_2154'),
        ('registro_hora_extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='colaborador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='colaboradores.Colaborador'),
            preserve_default=False,
        ),
    ]
