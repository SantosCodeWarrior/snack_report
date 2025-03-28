# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0013_remove_journal_master_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_master',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
