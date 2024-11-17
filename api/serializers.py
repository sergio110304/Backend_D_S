from rest_framework import serializers
from .models import Users, User_profiles, Place_categories, Tourist_places, Itineraries, Reviews

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 
                  'email', 
                  'first_name', 
                  'last_name', 
                  'created_at', 
                  'last_login',
                  'password_hash', 
                  'account_status']
        read_only_fields = ['user_id', 'created_at', 'last_login']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profiles
        fields = ['profile_id', 
                  'user_id', 
                  'profile_picture_url', 
                  'phone_number', 
                  'language_preference', 
                  'timezone', 
                  'notification_preferences', 
                  'last_updated']
        read_only_fields = ['profile_id', 'user_id', 'last_updated']

class PlaceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Place_categories
        fields = ['category_id', 
                  'name', 
                  'description', 
                  'icon_url', 
                  'parent_category_id',
                  'created_at']
        read_only_fields = ['category_id', 'created_at']

class TouristPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist_places
        fields = ['place_id', 
                  'name', 
                  'description', 
                  'category_id', 
                  'latitude', 
                  'longitude', 
                  'address', 
                  'average_duration', 
                  'cost_level', 
                  'accessibility_features', 
                  'contact_info', 
                  'website', 
                  'images',
                  'created_at',
                  'updated_at', 
                  'status']
        read_only_fields = ['place_id', 'category_id', 'created_at', 'updated_at']


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itineraries
        fields =['itinerary_id', 
                 'user_id', 
                 'name', 
                 'description', 
                 'start_date', 
                 'end_date', 
                 'total_distance', 
                 'estimated_cost',
                 'created_at',
                 'last_modified', 
                 'status']
        read_only_fields = ['itinerary_id', 'user_id', 'created_at', 'last_modified']

class ReviewSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)
    place_id = TouristPlaceSerializer(read_only=True)

    class Meta:
        model = Reviews
        fields = ['review_id', 
                  'user_id', 
                  'place_id',
                  'itinerary_id', 
                  'rating', 
                  'comment', 
                  'visit_date', 
                  'created_at', 
                  'status']
        read_only_fields = ['review_id', 'created_at', 'user_id', 'place_id', 'itinerary_id']
