# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 18:30
from __future__ import unicode_literals

from django.db import migrations

def load_data(apps, schema_editor):
	"""Load data in from other db"""
	PlayerStat = apps.get_model("app", "PlayerStat")
	PlayerStat(player_name='Julian Edleman', rec=17, yds=153, yds_rec=9.0,
				longest_yds=19, touchdowns=0).save()
	PlayerStat(player_name='Rob Gronkowski', rec=15, yds=227, yds_rec=15.1,
				longest_yds=40, touchdowns=3).save()
	PlayerStat(player_name='James White', rec=7, yds=84, yds_rec=12.0,
				longest_yds=29, touchdowns=0).save()
	PlayerStat(player_name='Danny Amendola', rec=7, yds=57, yds_rec=8.1,
				longest_yds=16, touchdowns=0).save()
	PlayerStat(player_name='Brandon Bolden', rec=3, yds=26, yds_rec=8.7,
				longest_yds=20, touchdowns=0).save()
	PlayerStat(player_name='Brandon LaFell', rec=3, yds=6, yds_rec=2.0,
				longest_yds=9, touchdowns=0).save()
	PlayerStat(player_name='Keshawn Martin', rec=2, yds=57, yds_rec=28.5,
				longest_yds=42, touchdowns=0).save()
	PlayerStat(player_name='Steven Jackson', rec=1, yds=2, yds_rec=2.0,
				longest_yds=2, touchdowns=0).save()

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160222_1826'),
    ]

    operations = [
    	migrations.RunPython(load_data)
    ]
