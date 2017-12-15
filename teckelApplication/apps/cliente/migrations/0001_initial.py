# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-15 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=50)),
                ('apellidoCliente', models.CharField(max_length=50)),
                ('cedulaCliente', models.IntegerField()),
                ('barrioCliente', models.CharField(max_length=50)),
                ('direccionCliente', models.CharField(max_length=50)),
                ('correoCliente', models.EmailField(max_length=254)),
                ('contraseñaCliente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPedido', models.CharField(max_length=50)),
                ('domicilioPedido', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='pedido',
            field=models.ManyToManyField(to='cliente.Pedido'),
        ),
    ]
