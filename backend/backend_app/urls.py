from django.urls import path
from .views import plotly_histogram, import_data

urlpatterns = [
    path('histogram/', plotly_histogram, name='plotly_histogram'),
    path('data/', import_data, name='data'),
]
