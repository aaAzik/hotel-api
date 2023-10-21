from django.contrib import admin
from apps.room.models import *

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)