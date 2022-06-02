# Generated by Django 4.0.4 on 2022-05-30 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_turnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('nacimiento', models.DateField()),
                ('turno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesionales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('especialidad', models.CharField(max_length=40)),
                ('turno', models.IntegerField()),
            ],
        ),
    ]
