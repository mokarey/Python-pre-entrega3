# Generated by Django 4.2.1 on 2023-05-24 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('juegosApp', '0006_alter_paygames_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paygames',
            name='imagen',
        ),
    ]
