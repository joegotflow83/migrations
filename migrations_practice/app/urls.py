from django.conf.urls import url

from app import views


urlpatterns = [
	url(r'^$', views.PlayerList.as_view(), name='list_players'),
	url(r'^(?P<pk>\d+)/$', views.DetailPlayer.as_view(), name='detail_player'),
]