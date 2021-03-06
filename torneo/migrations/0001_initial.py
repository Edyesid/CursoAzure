# Generated by Django 2.2.2 on 2019-07-04 14:27

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitan',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tipoDocumento', models.CharField(choices=[('CC', 'Cedula Ciudadania'), ('TI', 'Tarjeta Identidad'), ('CE', 'Cedula Extranjeria')], default='CC', max_length=2)),
                ('numeroDocumento', models.CharField(max_length=11)),
                ('carne', models.CharField(max_length=7)),
                ('afinacion', models.CharField(choices=[('Pregrado', 'Pregrado'), ('Posgrado', 'Posgrado'), ('Graduado', 'Graduado'), ('Profesor', 'Profesor'), ('Personal Administrativo', 'Personal Administrativo')], default='Pregrado', max_length=23)),
                ('celular', models.CharField(max_length=10)),
                ('semestre', models.CharField(max_length=2, null=True)),
                ('semestreGrado', models.CharField(max_length=6, null=True)),
                ('nombreEquipo', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=200)),
                ('apellidoCompleto', models.CharField(max_length=200)),
                ('semestre', models.CharField(max_length=2)),
                ('carne', models.CharField(max_length=7)),
                ('capitan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.Capitan')),
            ],
        ),
    ]
