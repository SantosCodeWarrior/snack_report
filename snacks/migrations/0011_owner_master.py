# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0010_remove_journal_master_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='owner_master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('contact_no', models.CharField(max_length=200, null=True)),
                ('shop_name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
