from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# room can only have one topic
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True) #every time database is saved , go ahead and take the screenshot
    created = models.DateTimeField(auto_now_add=True) #record timestap when instance is creared at first
    
    def __str__(self) :
        return self.name

# Message will have one to many reln with Room

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room , on_delete=models.CASCADE) #when a room is deleted , delete all the messages in that room
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #every time database is saved , go ahead and take the screenshot
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.body[0:50]