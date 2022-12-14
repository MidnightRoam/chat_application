from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from .models import Room, Message


@method_decorator(login_required, name='dispatch')
class RoomsListView(ListView):
    """Render list of created rooms"""
    template_name = 'room_list.html'
    context_object_name = 'rooms'
    paginate_by = 5

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
def RoomView(request, room_name):
    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=room)
    users = User.objects.all().count()

    return render(request, 'room/chat.html', {'room': room, 'messages': messages, 'users': users})


def create_room(request):
    # Если ввести название комнаты и в конце будет стоять знак ! - этот знак обрежется
    # Если в названии комнаты есть пробел - он будет изменен на _
    room = request.POST.get('room_name').rstrip('!').replace(' ', '_')

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room)
    else:
        slug = room.replace(' ', '-').lower()
        new_room = Room.objects.create(name=room, slug=slug)
        new_room.save()
        return redirect('/' + room + '/')
