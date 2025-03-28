# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0003_standard_snacks_list_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_type', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='expense_master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('items_type', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tiffin_master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiffin_type', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vendor_master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor_name', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('contact_no', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
