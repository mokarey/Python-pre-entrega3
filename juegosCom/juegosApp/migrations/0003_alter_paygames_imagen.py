# Generated by Django 4.2.1 on 2023-05-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegosApp', '0002_paygames_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paygames',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
