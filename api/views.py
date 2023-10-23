from django.shortcuts import render
from apps.hotel.models import *
from apps.room.models import *
from apps.booking.models import *
from apps.guest.models import *
from rest_framework.status import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers(partial=True)
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers(partial=True)
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers(partial=True)
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers(partial=True)
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]