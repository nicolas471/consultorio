# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birthdate', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ForeignKey(to='consultorio_index.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('direction', models.CharField(max_length=30)),
                ('borough', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='play',
            name='current_theater',
            field=models.ForeignKey(to='consultorio_index.Theatre'),
        ),
        migrations.AddField(
            model_name='play',
            name='genre',
            field=models.ForeignKey(to='consultorio_index.Genre'),
        ),
        migrations.AddField(
            model_name='play',
            name='members',
            field=models.ManyToManyField(to='consultorio_index.Member'),
        ),
        migrations.AddField(
            model_name='play',
            name='pictures_book',
            field=models.ManyToManyField(to='consultorio_index.Image'),
        ),
        migrations.AddField(
            model_name='member',
            name='rol',
            field=models.ForeignKey(to='consultorio_index.Rol'),
        ),
    ]
