# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0005_tiffin_master_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='journal_master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiffin_type', models.CharField(max_length=200, null=True)),
                ('rate', models.FloatField(null=True)),
                ('entry_date', models.DateField(null=True)),
                ('tiffin_breakfast_qty', models.IntegerField(default=0, null=True)),
                ('tiffin_lunch_qty', models.IntegerField(default=0, null=True)),
                ('tiffin_dinner_qty', models.IntegerField(default=0, null=True)),
                ('tiffin_total', models.FloatField(null=True)),
                ('qty', models.IntegerField(default=0, null=True)),
                ('amount', models.FloatField(null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snacks.master_register', null=True)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snacks.standard_snacks_list', null=True)),
            ],
        ),
    ]
