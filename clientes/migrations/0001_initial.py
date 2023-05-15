# Generated by Django 4.2.1 on 2023-05-14 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=60)),
                ('Correo', models.EmailField(max_length=254)),
                ('TipoCliente', models.CharField(max_length=50)),
            ],
        ),
    ]
