# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-19 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='certificate',
            name='organization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='certificate.Organization'),
        ),
    ]
