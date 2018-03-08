# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-19 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patchwork', '0021_django_1_10_fixes'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subject_match',
            field=models.CharField(blank=True, default=b'', help_text=b'Regex to match the subject against if only part of emails sent to the list belongs to this project. Will be used with IGNORECASE and MULTILINE flags. If rules for more projects match the first one returned from DB is chosen; empty field serves as a default for every email which has no other match.', max_length=64),
        ),
        migrations.AlterField(
            model_name='project',
            name='listid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('listid', 'subject_match')]),
        ),
    ]