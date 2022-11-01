from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RoomsListView, RoomView

urlpatterns = [
        path('chats/', RoomsListView.as_view(), name='chats'),
        path('<slug:slug>/', RoomView, name='chat')
]
