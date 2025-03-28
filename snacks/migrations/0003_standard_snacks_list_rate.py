# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_standard_snacks_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='standard_snacks_list',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
