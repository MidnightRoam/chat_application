from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .models import Room, Message


@method_decorator(login_required, name='dispatch')
class RoomsListView(ListView):
    """Render list of created rooms"""
    template_name = 'room_list.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return Room.objects.all()


# @method_decorator(login_required, name='dispatch')
# class RoomView(DetailView):
#     """Detail room view"""
#     model = Room
#     template_name = 'room/chat.html'
#     context_object_name = {'room', 'messages'}
#     slug_field = 'slug'
#     room = Room.objects.get(slug=slug_field)
#     messages = Message.objects.filter(room=room)

    # def get_queryset(self, slug):
    #     room = Room.objects.get(slug=slug)
    #     messages = Message.objects.filter(room=room)

@login_required
def RoomView(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'room/chat.html', {'room': room, 'messages': messages})