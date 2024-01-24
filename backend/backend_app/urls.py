from django.urls import path
from .views import plotly_histogram, diet_adaptation, popularity_diet, distrib_restaurant_régimes, plotly_bar_chart, box_plot_service, box_plot_value, box_plot_atmosphere

urlpatterns = [
    path('restaurants-country/', plotly_histogram, name='plotly_histogram'),
    path('price-diet/', diet_adaptation, name='diet_adaptation'),
    path('price-diet/', diet_adaptation, name='diet_adaptation'),
    path('popularity-diet/', popularity_diet, name='popularity_diet'),
    path('distribution-restaurants/', distrib_restaurant_régimes, name='distrib_restaurant_régimes'),
    path('distribution-cuisine/', plotly_bar_chart, name='plotly_bar_chart'),

    # Bakari 
    path('plot-service/', box_plot_service, name='box_plot_service'),
    path('plot-value/', box_plot_value, name='box_plot_value'),
    path('plot-atmosphere/', box_plot_atmosphere, name='box_plot_atmosphere'),
]
