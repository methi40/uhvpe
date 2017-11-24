# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 09:07
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_workshopregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Event')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='workshopregistration',
            unique_together=set([('workshop', 'email')]),
        ),
        migrations.AlterUniqueTogether(
            name='eventregistration',
            unique_together=set([('event', 'email')]),
        ),
    ]