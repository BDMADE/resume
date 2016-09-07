# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=250)),
                ('department', models.CharField(blank=True, max_length=250, null=True)),
                ('present', models.BooleanField(default=False)),
                ('joining_date', models.DateField()),
                ('ending_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.Experience')),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.Organization'),
        ),
    ]
