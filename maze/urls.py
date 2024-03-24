from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='maze-home'),
    path('play/', views.play, name='maze-play'),
    path('get-maze/', views.get_maze_json, name='maze-get_json_file'),
    path('test20240324/', views.test, name='maze-test'),
]

