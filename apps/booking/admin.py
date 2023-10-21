from django.contrib import admin
from apps.booking.models import *

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)