from django.db import models


class PlayerStat(models.Model):


	player_name = models.CharField(max_length=32)
	rec = models.IntegerField(default=0)
	yds = models.IntegerField(default=0)
	yds_rec = models.FloatField(default=0.0)
	longest_yds = models.IntegerField(default=0)
	touchdowns = models.IntegerField(default=0)