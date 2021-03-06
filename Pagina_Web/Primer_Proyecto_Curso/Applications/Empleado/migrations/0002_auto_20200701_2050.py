# Generated by Django 3.0 on 2020-07-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Mi Habilidad',
                'verbose_name_plural': 'Habilidades de los empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-first_name'], 'verbose_name': 'Mi Empleado',
                     'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
