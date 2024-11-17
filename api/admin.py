from django.contrib import admin
from .models import Users, User_profiles, User_preferences, Place_categories, Tourist_places, Place_schedules, Special_events, Itineraries, ItineraryDetail, Reviews, Realtime_data, Usage_statistics

# Register your models here.

admin.site.register(Users)
admin.site.register(User_profiles)
admin.site.register(User_preferences)
admin.site.register(Place_categories)
admin.site.register(Tourist_places)
admin.site.register(Place_schedules)
admin.site.register(Special_events)
admin.site.register(Itineraries)
admin.site.register(ItineraryDetail)
admin.site.register(Reviews)
admin.site.register(Realtime_data)
admin.site.register(Usage_statistics)
