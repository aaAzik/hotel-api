from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView)

urlpatterns = [ 
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view())
    ]

router = DefaultRouter()
router.register('hotel', HotelViewSet, basename='hotel')
router.register('room', RoomViewSet, basename='room')
router.register('guest', GuestViewSet, basename='guest')
router.register('booking', BookingViewSet, basename='booking')

urlpatterns += router.urls