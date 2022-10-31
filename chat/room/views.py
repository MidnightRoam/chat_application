from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .models import Room


@method_decorator(login_required, name='dispatch')
class RoomsListView(ListView):
    """Render list of created rooms"""
    template_name = 'room_list.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        return Room.objects.all()


@method_decorator(login_required, name='dispatch')
class RoomView(DetailView):
    """Detail room view"""
    model = Room
    template_name = 'room/chat.html'
    context_object_name = 'room'
    slug_field = 'slug'
