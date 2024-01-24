from django.urls import path
from .views import plotly_histogram, diet_adaptation, popularity_diet, distrib_restaurant_régimes, plotly_bar_chart, plotly_box_chart, noteMoyenneNbreRestau

urlpatterns = [
    path('restaurants-country/', plotly_histogram, name='plotly_histogram'),
    path('price-diet/', diet_adaptation, name='diet_adaptation'),
    path('price-diet/', diet_adaptation, name='diet_adaptation'),
    path('popularity-diet/', popularity_diet, name='popularity_diet'),
    path('distribution-restaurants/', distrib_restaurant_régimes, name='distrib_restaurant_régimes'),
    path('distribution-cuisine/', plotly_bar_chart, name='plotly_bar_chart'),
    path('distribution-satisfaction/', plotly_box_chart, name='plotly_box_chart'),
    path('note-moyenne-restaurants/', noteMoyenneNbreRestau, name='noteMoyenneNbreRestau'),
    # path('note-top-eight/', radar_chart, name='radar_chart'),
]
