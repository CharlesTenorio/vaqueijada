# Generated by Django 4.0.6 on 2022-07-30 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vaqueiros', '0001_initial'),
        ('formapg', '0001_initial'),
        ('eventos', '0001_initial'),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Senha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.CharField(max_length=4)),
                ('adquirida', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senha', models.TextField(max_length=200)),
                ('esteira_vaqueiro', models.CharField(max_length=50)),
                ('representacao', models.CharField(max_length=80)),
                ('cidade', models.CharField(max_length=50)),
                ('cavalo', models.CharField(max_length=40)),
                ('esteira_cavalo', models.CharField(max_length=40)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categoria.categoria')),
                ('evento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='eventos.evento')),
                ('forma_pg', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='formapg.formapg')),
                ('vaqueiro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaqueiros.vaqueiro')),
            ],
        ),
    ]
