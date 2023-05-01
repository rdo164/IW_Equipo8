# Generated by Django 4.2 on 2023-05-01 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=200)),
                ('fecha_adquisicion', models.DateField()),
                ('fecha_instalacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codOrdenFabricacion', models.IntegerField(default=0)),
                ('codigoProceso', models.IntegerField(default=0)),
                ('nombreProceso', models.CharField(max_length=100)),
                ('referencia', models.CharField(max_length=100)),
                ('fechaInicio', models.DateTimeField()),
                ('fechaFin', models.DateTimeField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEmpresaGrupo8.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEmpresaGrupo8.equipo')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appEmpresaGrupo8.proceso')),
            ],
        ),
    ]
