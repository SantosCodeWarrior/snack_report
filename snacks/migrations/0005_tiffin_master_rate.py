# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0004_billing_expense_master_tiffin_master_vendor_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiffin_master',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
