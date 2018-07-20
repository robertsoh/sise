# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-20 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EAP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('codigo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('codigo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.AddField(
            model_name='eap',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eaps', to='facultades.Facultad'),
        ),
    ]
