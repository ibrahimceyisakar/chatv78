from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="rooms", blank=True)

    def get_online_count(self):
        return self.users.filter(is_online=True).count()

    def __str__(self):
        return f"{self.name} - {self.get_online_count()}"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room.name} - {self.content}"
