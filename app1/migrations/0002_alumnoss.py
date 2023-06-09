# Generated by Django 3.2.8 on 2023-04-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alumnoss',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('tipoidentificacion', models.CharField(max_length=30)),
                ('numeroid', models.CharField(max_length=30)),
                ('fechanacimiento', models.DateField(null='True')),
                ('semestre', models.IntegerField()),
                ('fecharegistro', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'alumnoss',
            },
        ),
    ]
