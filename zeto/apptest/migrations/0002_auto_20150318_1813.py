# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='hola', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
    ]
