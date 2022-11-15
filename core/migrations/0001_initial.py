# Generated by Django 4.1.1 on 2022-10-09 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('placa', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('año', models.IntegerField(blank=True, null=True)),
                ('combustible', models.CharField(max_length=30)),
                ('kilometraje', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('transmision', models.CharField(max_length=30)),
                ('carroceria', models.CharField(max_length=30)),
                ('motor', models.CharField(max_length=30)),
                ('cilindraje', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='encargado',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mantenimiento',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=500)),
                ('kilometraje', models.IntegerField()),
                ('estado', models.CharField(max_length=30)),
                ('servicio', models.CharField(max_length=30)),
                ('nota', models.CharField(max_length=500)),
                ('encargado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.encargado')),
                ('placa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carro')),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('correo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('detail', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='taller',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('carro', models.ManyToManyField(blank=True, null=True, to='core.carro')),
            ],
        ),
        migrations.CreateModel(
            name='repuesto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('referencia', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('mantenimientoId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.mantenimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento_Detalle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('costo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('mantenimientoId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.mantenimiento')),
            ],
        ),
        migrations.AddField(
            model_name='encargado',
            name='tallerId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.taller'),
        ),
        migrations.AddField(
            model_name='carro',
            name='propietarioId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.propietario'),
        ),
    ]