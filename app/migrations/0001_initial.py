# Generated by Django 3.1.2 on 2021-04-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='mamografias')),
            ],
        ),
    ]