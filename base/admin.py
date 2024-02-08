from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.

class MessagesAdmin(admin.ModelAdmin):
    list_display=('MESSAGE', 'print_image')

from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
