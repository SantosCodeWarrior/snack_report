# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0007_remove_journal_master_tiffin_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal_master',
            name='rate',
        ),
    ]
