from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RoomsListView, RoomView, checkview

urlpatterns = [
        path('chats/', RoomsListView.as_view(), name='chats'),
        path('<str:room_name>/', RoomView, name='chat'),
        path('checkview', checkview, name='checkview')
]
