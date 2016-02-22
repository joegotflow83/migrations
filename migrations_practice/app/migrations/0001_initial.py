# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=32)),
                ('rec', models.IntegerField(default=0)),
                ('yds', models.IntegerField(default=0)),
                ('yds_rec', models.FloatField(default=0.0)),
                ('longest_yds', models.IntegerField(default=0)),
                ('touchdowns', models.IntegerField(default=0)),
            ],
        ),
    ]
