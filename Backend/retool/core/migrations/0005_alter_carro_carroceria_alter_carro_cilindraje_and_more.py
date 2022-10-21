# Generated by Django 4.1.1 on 2022-10-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_carro_propietarioid_carro_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='carroceria',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='cilindraje',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='color',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='combustible',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='kilometraje',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='marca',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='modelo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='motor',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='transmision',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
