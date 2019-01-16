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
	
]
