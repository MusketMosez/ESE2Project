from django.urls import path

from . import views

urlpatterns = [
    path('save_log', views.save_log, name='save log'),
]
