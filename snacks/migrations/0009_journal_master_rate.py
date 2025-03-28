# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0008_remove_journal_master_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal_master',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
