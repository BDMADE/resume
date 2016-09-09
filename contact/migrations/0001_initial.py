# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('icon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='icon.Icon')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('details', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='icon.Icon')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='types',
            field=models.ManyToManyField(to='contact.Type'),
        ),
    ]
