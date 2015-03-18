# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0002_auto_20150318_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.RunSQL("UPDATE apptest_customer SET address=name || '- No address provided';")
    ]
