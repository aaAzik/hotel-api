from django.shortcuts import render
from apps.hotel.models import *
from apps.room.models import *
from apps.booking.models import *
from apps.guest.models import *
from rest_framework.status import *
from .serializer import *
from .serializer import HotelSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]