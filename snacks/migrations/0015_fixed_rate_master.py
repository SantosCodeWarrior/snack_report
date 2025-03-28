# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0014_owner_master_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='fixed_rate_master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.FloatField(null=True)),
            ],
        ),
    ]
