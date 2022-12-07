from django.contrib import admin

from .models import Room, Topic, Message, Profile

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)
admin.site.register(Profile)
