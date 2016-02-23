from django.views.generic import ListView, TemplateView, DetailView

from .models import PlayerStat


class Index(TemplateView):


	template_name = 'app/index.html'


class PlayerList(ListView):


	model = PlayerStat


class DetailPlayer(DetailView):


	queryset = PlayerStat.objects.all()
	template_name = 'app/player.html'

	def get_object(self):
		"""Grab the specific player object"""
		object = super().get_object()
		return object