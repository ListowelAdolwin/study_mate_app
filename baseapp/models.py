from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) #This establishes a many to many relationship between room and participants
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        This class specifies the order in which objects of the class are arranged(prioritised).
        In the example below, the ordering is based on updated, and then created, but in reverse order.(The latest updated
        will appear first.
        """
        ordering = ['-updated', '-created']


    def __str__(self):
        """
        How an object of this class should be displayed(Display it by its name attribute)"""
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=200)
    last_name = models.CharField( null=True, max_length=200)
    avatar = models.ImageField(default='default_avatar.jpg', upload_to='profile_images')
    header = models.ImageField(default='default_header.png', upload_to='profile_images')
    bio = models.TextField(null=True, blank=True)
    bookmarks = models.ManyToManyField(Message, related_name='bookmarks', blank=True)


    def __str__(self):
        return self.user.username
