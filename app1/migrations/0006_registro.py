# Generated by Django 3.2.8 on 2023-04-13 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20230407_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.alumnos')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.cursos')),
            ],
            options={
                'db_table': 'registros',
            },
        ),
    ]
