from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Users, User_profiles, Place_categories, Tourist_places, Itineraries, Reviews
from .serializers import UserSerializer, UserProfileSerializer, PlaceCategorySerializer, TouristPlaceSerializer, ItinerarySerializer, ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User_profiles.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


class PlaceCategoryViewSet(viewsets.ModelViewSet):
    queryset = Place_categories.objects.all()
    serializer_class = PlaceCategorySerializer
    permission_classes = [permissions.AllowAny]

class TouristPlaceViewSet(viewsets.ModelViewSet):
    queryset = Tourist_places.objects.all()
    serializer_class = TouristPlaceSerializer
    permission_classes = [permissions.AllowAny]


class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itineraries.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [permissions.AllowAny]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

