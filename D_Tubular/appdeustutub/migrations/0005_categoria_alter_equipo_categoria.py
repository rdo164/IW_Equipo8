# Generated by Django 4.2 on 2023-05-24 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appdeustutub', '0004_alter_equipo_categoria_delete_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='equipo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appdeustutub.categoria'),
        ),
    ]