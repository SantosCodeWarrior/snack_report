# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0009_journal_master_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal_master',
            name='rate',
        ),
    ]
