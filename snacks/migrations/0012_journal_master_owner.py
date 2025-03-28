# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0011_owner_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal_master',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snacks.owner_master', null=True),
        ),
    ]
