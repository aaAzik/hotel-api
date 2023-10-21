from rest_framework import serializers
from apps.booking.models import *
from apps.guest.models import *
from apps.hotel.models import *
from apps.room.models import *

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking   
        fields = '__all__'


class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'