from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True)
    created_at = models.DateField(default=timezone.now())

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} | {self.room}"

    class Meta:
        ordering = ('created_at',)
