from django.urls import path
from .views import *

urlpatterns = [
    path('preference/', preference, name='preference'),
    path('model/', model, name='model'),
    path('get-restaurants/', get_recommended_restaurants, name='get_recommended_restaurants'),
    path('get-regions/', get_regions, name='get_regions'),

    path('numbers/', numRestaurants, name='numRestaurants'),
    
    path('restaurants-country/', plotly_histogram, name='plotly_histogram'),
    path('price-diet/', diet_adaptation, name='diet_adaptation'),
    path('popularity-diet/', popularity_diet, name='popularity_diet'),
    path('distribution-restaurants/', distrib_restaurant_regimes, name='distrib_restaurant_regimes'),

    # Bakari 
    path('plot-service/', box_plot_service, name='box_plot_service'),
    path('plot-value/', box_plot_value, name='box_plot_value'),
    path('plot-atmosphere/', box_plot_atmosphere, name='box_plot_atmosphere'),
    path('distribution-satisfaction/', plotly_bar_chart, name='plotly_bar_chart'),

    # Kemo
    path('note-moyenne-restaurants/', noteMoyenneNbreRestau, name='noteMoyenneNbreRestau'),
    path('note-top-eight/', radar_chart, name='radar_chart'),
]
