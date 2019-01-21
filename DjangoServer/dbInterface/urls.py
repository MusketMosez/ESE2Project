from django.urls import path

from . import views

urlpatterns = [
    path('save-log', views.save_log, name='save log'),
	path('bldg/<slug:id>/', views.bldg, name='bldg'),
	path('bldg/<slug:name>/', views.bldg, name='get bldg by name')
	path('add-bldg', views.add_bldg, name='add bldg'),
	path('add-room', views.add_room, name='add room'),
	path('add-sensor', views.add_sensor, name='add sensor'),
	path('get-all-rooms', views.get_all_rooms, name='get all rooms'),
    path('get-all-rooms-logs', views.get_all_rooms_logs, name='get all rooms logs'),
	path('room/<slug:name>/', views.room, name='room'),
	path('room/get-room-logs/', views.get_room_logs, name='get room logs'),
	path('bldg/<slug:id>/get-rooms-by-bldg', views.get_rooms_by_bldg, name='get rooms by bldg'),
	path('room/<slug:name>/get-sensors-in-room/', views.get_sensors_in_room, name='get sensors in room'),
	path('log', views.log, name='log'),
	path('save-logs', views.save_log, name='save logs'),
	path('sensor/<slug:id>/', views.sensor, name='sensor'),
	
	
]
