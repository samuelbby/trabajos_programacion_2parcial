# Generated by Django 4.1.7 on 2023-03-17 00:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='address',
            field=models.CharField(help_text='Ingrese la direccion del proveedor', max_length=255, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='city',
            field=models.CharField(choices=[('1801', 'Yoro'), ('1806', 'Morazán'), ('1805', 'Jocón')], help_text='Seleccione la ciudad del proveedor', max_length=4, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.CharField(help_text='Ingrese el correo electronico del proveedor', max_length=70, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='name',
            field=models.CharField(help_text='Ingrese el nombre del proveedor', max_length=150, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='phone',
            field=models.CharField(help_text='Ingrese el correo del proveedor', max_length=8, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='rtn',
            field=models.CharField(help_text='Ingrese el RTN del proveedor', max_length=14, verbose_name='RTN'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='status',
            field=models.BooleanField(default=True, help_text='Seleccione el estado del proveedor', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='UUID'),
        ),
    ]