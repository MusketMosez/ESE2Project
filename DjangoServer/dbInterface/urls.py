from django.urls import path

from . import views

urlpatterns = [
    path('save_log', views.save_log, name='save log'),
	path('bldg/<slug:id>/', views.bldg, name='bldg'),
	path('bldg/<slug:name>/', views.bldg, name='get bldg by name')
	path('add_bldg', views.add_bldg, name='add bldg'),
	path('add_room', views.add_room, name='add room'),
	path('add_sensor', views.add_sensor, name='add sensor'),
	path('get_all_rooms', views.get_all_rooms, name='get all rooms'),
    path('get_all_rooms_logs', views.get_all_rooms_logs, name=
	
]
