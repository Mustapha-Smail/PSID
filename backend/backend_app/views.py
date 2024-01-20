import plotly
import plotly.graph_objs as go
import plotly.express as px
import random
import json
from django.http import JsonResponse
import pandas as pd
from .data.load_data import data_frame 


def import_data(request): 
    vegan_counts = data_frame['vegetarian_friendly'].value_counts()
    vegan_counts.index = ['Vegetarian Friendly' if x == 'Y' else 'Not Vegetarian Friendly' for x in vegan_counts.index]

    fig = px.pie(vegan_counts, values=vegan_counts.values, names=vegan_counts.index, title='Ratio of Vegetarian-Friendly Restaurants')
    
    # Convert the figure to JSON
    pieJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return JsonResponse({"data": pieJSON})


def plotly_histogram(request):
    country_counts = data_frame['country'].value_counts()

    fig = px.bar(country_counts, x=country_counts.index, y=country_counts.values, labels={'x': 'Country', 'y': 'Number of Restaurants'})
    fig.update_layout(title_text='Number of Restaurants per Country', xaxis_tickangle=-45)

    # Convert the figure to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({"data": graphJSON})
