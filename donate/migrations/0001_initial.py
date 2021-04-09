# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-04-09 06:52
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Class', models.IntegerField(validators=[django.core.validators.MaxValueValidator(13), django.core.validators.MinValueValidator(1)])),
                ('Publisher', models.CharField(max_length=200)),
                ('Edition', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Forth', 'Forth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth'), ('Ninth', 'Ninth'), ('Tenth', 'Tenth')], max_length=10)),
                ('Status', models.CharField(choices=[('Open', 'Open'), ('Reserved', 'Reserved')], max_length=10)),
                ('Your_District', models.CharField(max_length=100)),
                ('Ward_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(36), django.core.validators.MinValueValidator(1)])),
                ('Phone_number', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Details2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Class', models.CharField(blank=True, max_length=200, null=True)),
                ('Publisher', models.CharField(max_length=200)),
                ('Edition', models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Forth', 'Forth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth'), ('Ninth', 'Ninth'), ('Tenth', 'Tenth')], max_length=10)),
                ('Status', models.CharField(choices=[('Open', 'Open'), ('Reserved', 'Reserved')], max_length=10)),
                ('Your_Address', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]