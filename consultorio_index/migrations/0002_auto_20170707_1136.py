# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio_index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(verbose_name='images', upload_to=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='play',
            name='release_date',
            field=models.DateField(),
        ),
    ]
