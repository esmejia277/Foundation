# Generated by Django 2.2.2 on 2019-07-05 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Celular')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['-name'],
            },
        ),
    ]
