from django.contrib import admin

from .models import PlayerStat


@admin.register(PlayerStat)
class PlayerStatAdmin(admin.ModelAdmin):


	pass