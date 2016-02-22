# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 17:56
from __future__ import unicode_literals

from django.db import migrations

def combine_names(apps, schema_editor):
	"""Migrate data in other db"""
	stats = [
	('Julian Edleman', 17, 153, 9.0, 19, 0),
	('Rob Gronkowski', 15, 227, 15.1, 40, 3),
	('James White', 7, 84, 12.0, 29, 0),
	('Danny Amendola', 7, 57, 8.1, 16, 0),
	('Brandon Bolden', 3, 26, 8.7, 20, 0),
	('Brandon LaFell', 3, 6, 2.0, 9, 0),
	('Keshawn Martin', 2, 57, 28.5, 42, 0),
	('Steven Jackson', 1, 2, 2.0, 2, 0)
	]
	PlayerStat = apps.get_model("app", "PlayerStat")
	for index, player in enumerate(PlayerStat.objects.all()):
		player.player_name = '{}'.format(stats[index][0])
		player.rec = '{}'.format(stats[index][1])
		player.yds = '{}'.format(stats[index][2])
		player.yds_rec = '{}'.format(stats[index][3])
		player.longest_yds = '{}'.format([index][4])
		player.touchdowns = '{}'.format([index][5])
		player.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160222_1737'),
    ]

    operations = [
    	migrations.RunPython(combine_names)
    ]
