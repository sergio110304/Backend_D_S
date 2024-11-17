from rest_framework import routers
from .views import UserViewSet, UserProfileViewSet, PlaceCategoryViewSet, TouristPlaceViewSet, ItineraryViewSet, ReviewViewSet

router = routers.DefaultRouter()

router.register('api/users', UserViewSet, 'users')

router.register('api/user_profiles', UserProfileViewSet, 'user_profiles')

router.register('api/place_categories', PlaceCategoryViewSet, 'place_categories')

router.register('api/tourist_places', TouristPlaceViewSet, 'tourist_places')

router.register('api/itineraries', ItineraryViewSet, 'itineraries')

router.register('api/reviews', ReviewViewSet, 'reviews')

urlpatterns = router.urls
