# Generated by Django 4.2.1 on 2023-05-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegosApp', '0007_remove_paygames_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paygames',
            name='lanzamiento',
            field=models.DateField(),
        ),
    ]