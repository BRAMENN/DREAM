# Generated by Django 3.1.2 on 2021-05-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mamography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(null=True, upload_to='mamografias')),
                ('birad', models.CharField(max_length=50, verbose_name='tipo de cancer')),
            ],
            options={
                'verbose_name': 'mamografia',
                'verbose_name_plural': 'mamografias',
                'ordering': ['birad'],
            },
        ),
        migrations.AlterModelOptions(
            name='medico',
            options={'ordering': ['id'], 'verbose_name': 'Medico', 'verbose_name_plural': 'Medicos'},
        ),
        migrations.RemoveField(
            model_name='medico',
            name='imagen',
        ),
    ]
