# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0007_auto_20181013_1041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Reviews',
        ),
    ]
