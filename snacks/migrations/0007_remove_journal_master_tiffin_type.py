# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0006_journal_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal_master',
            name='tiffin_type',
        ),
    ]
