from django.db import models

# Create your models here.

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255, null=True, blank=True)
    verification_token_expires = models.DateTimeField(null=True, blank=True)
    reset_password_token = models.CharField(max_length=255, null=True, blank=True)
    reset_password_expires = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    account_status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class User_profiles(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture_url = models.URLField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    language_preference = models.CharField(max_length=10, default='en')
    timezone = models.CharField(max_length=50)
    notification_preferences = models.JSONField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.first_name}"

class User_preferences(models.Model):
    preference_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, null=True, blank=True)
    cultural_interest = models.IntegerField(default=0)
    nature_interest = models.IntegerField(default=0)
    gastronomy_interest = models.IntegerField(default=0)
    shopping_interest = models.IntegerField(default=0)
    budget_level = models.IntegerField(default=0)
    accessibility_needs = models.BooleanField(default=False)
    preferred_transport = models.CharField(max_length=50)
    max_walking_distance = models.IntegerField()
    preferred_activity_times = models.JSONField(null=True, blank=True)
    special_interests = models.TextField()
    dietary_restrictions = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preferences of {self.user.first_name}"
    
class Place_categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_url = models.URLField(max_length=255, null=True, blank=True)
    parent_category_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tourist_places(models.Model):
    place_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Place_categories, on_delete=models.SET_NULL, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    address = models.TextField()
    average_duration = models.IntegerField()
    cost_level = models.IntegerField()
    accessibility_features = models.JSONField(null=True, blank=True)
    contact_info = models.JSONField(null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    images = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Place_schedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    place = models.ForeignKey(Tourist_places, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    special_hours = models.BooleanField(default=False)
    special_description = models.TextField(null=True, blank=True)
    seasonal_schedule = models.BooleanField(default=False)
    season_start = models.DateField(null=True, blank=True)
    season_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Schedule for {self.place.name}"
    
class Special_events(models.Model):
    event_id = models.AutoField(primary_key=True)
    place = models.ForeignKey(Tourist_places, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event: {self.name} at {self.place.name}"

class Itineraries(models.Model):
    itinerary_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_distance = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Itinerary: {self.name}"

class ItineraryDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    itinerary = models.ForeignKey(Itineraries, on_delete=models.CASCADE)
    place_id = models.ForeignKey(Tourist_places, on_delete=models.SET_NULL, null=True)
    visit_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    order_in_day = models.IntegerField()
    travel_mode = models.CharField(max_length=50)
    travel_duration = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Detail of {self.itinerary.name} at {self.place_id.name}"

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Tourist_places, on_delete=models.SET_NULL, null=True)
    itinerary = models.ForeignKey(Itineraries, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    images = models.TextField()
    visit_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Review by {self.user.first_name} for {self.place.name}"

class Realtime_data(models.Model):
    data_id = models.AutoField(primary_key=True)
    place = models.ForeignKey(Tourist_places, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField()
    crowd_level = models.IntegerField()
    weather_condition = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    waiting_time = models.IntegerField()
    special_notices = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Realtime data for {self.place.name} at {self.timestamp}"
    
class Usage_statistics(models.Model):
    stat_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    action_type = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=50)
    entiry_id = models.IntegerField()   
    timestamp = models.DateTimeField()
    additional_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Usage statistics for {self.user.first_name} at {self.timestamp}"
