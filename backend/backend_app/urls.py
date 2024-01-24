from django.urls import path
from .views import *

urlpatterns = [
    path('restaurants-country/', plotly_histogram, name='plotly_histogram'),
    path('price-diet/', diet_adaptation, name='diet_adaptation'),
    path('popularity-diet/', popularity_diet, name='popularity_diet'),
    path('distribution-restaurants/', distrib_restaurant_régimes, name='distrib_restaurant_régimes'),

    # Bakari 
    path('plot-service/', box_plot_service, name='box_plot_service'),
    path('plot-value/', box_plot_value, name='box_plot_value'),
    path('plot-atmosphere/', box_plot_atmosphere, name='box_plot_atmosphere'),
    path('distribution-satisfaction/', plotly_bar_chart, name='plotly_bar_chart'),
    path('note-moyenne-restaurants/', noteMoyenneNbreRestau, name='noteMoyenneNbreRestau'),
    # path('note-top-eight/', radar_chart, name='radar_chart'),
]
