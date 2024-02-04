from django.db import models

class Preference(models.Model): 
    PRICE_LEVEL_CHOICES = [
        ('€', '€'),
        ('€€-€€€', '€€-€€€'),
        ('€€€€', '€€€€'),
    ]
    
    AVG_RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    price_level = models.CharField(max_length=10, choices=PRICE_LEVEL_CHOICES)
    vegetarian_friendly = models.BooleanField(default=False)
    vegan_options = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    avg_rating = models.CharField(max_length=10, choices=AVG_RATING_CHOICES)
    

    # Override the save method to ensure there is only one record
    def save(self, *args, **kwargs):
        self.pk = 1  # Ensure that there is only one record with primary key 1
        super(Preference, self).save(*args, **kwargs)
    
class DataInsertionStatus(models.Model):
    has_data_been_inserted = models.BooleanField(default=False)
class Restaurant(models.Model):
    restaurant_link= models.TextField()
    restaurant_name= models.TextField()
    original_location= models.TextField()
    country        = models.TextField()
    region         = models.TextField()
    province       = models.TextField()
    city           = models.TextField()
    address        = models.TextField()
    latitude= models.TextField()
    longitude= models.TextField()
    claimed        = models.TextField()
    awards         = models.TextField()
    popularity_detailed= models.TextField()
    popularity_generic= models.TextField()
    top_tags= models.TextField()
    price_level= models.TextField()
    price_range   = models.TextField()
    meals          = models.TextField()
    cuisines       = models.TextField()
    special_diets  = models.TextField()
    features       = models.TextField()
    vegetarian_friendly= models.TextField()
    vegan_options  = models.TextField()
    gluten_free    = models.TextField()
    original_open_hours= models.TextField()
    open_days_per_week= models.TextField()
    open_hours_per_week= models.TextField()
    working_shifts_per_week= models.TextField()
    avg_rating= models.TextField()
    total_reviews_count= models.TextField()
    default_language= models.TextField()
    reviews_count_in_default_language= models.TextField()
    excellent= models.TextField()
    very_good= models.TextField()
    average= models.TextField()
    poor= models.TextField()
    terrible= models.TextField()
    food= models.TextField()
    service= models.TextField()
    value= models.TextField()
    atmosphere= models.TextField()
    keywords= models.TextField()
    
    def __str__(self):
        return self.restaurant_name



