from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RoomsListView, RoomView, create_room

urlpatterns = [
        path('chats/', RoomsListView.as_view(), name='chats'),
        path('<str:room_name>/', RoomView, name='chat'),
        path('create_room', create_room, name='create_room')
]
