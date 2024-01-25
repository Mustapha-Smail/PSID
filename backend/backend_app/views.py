import plotly
import plotly.graph_objs as go
import plotly.express as px
import math
import json
from django.http import JsonResponse
import pandas as pd
from .data.load_data import data_frame
import numpy as np
from collections import defaultdict

# Numbers
def numRestaurants(request): 
    df = data_frame.copy()
    total_restaurants = round(len(df), 2)
    average_rating = round(df['avg_rating'].mean(), 2)
    total_reviews = round(df['total_reviews_count'].sum(), 2)
    
    vegetarian_friendly_count = int((df['vegetarian_friendly'] == 'Y').sum())
    vegan_options_count = int((df['vegan_options'] == 'Y').sum())
    gluten_free_count = int((df['gluten_free'] == 'Y').sum())

    summary_data = [
        {"title": "Restaurants","value": total_restaurants},
        {"title": "Note moyenne", "value": average_rating},
        {"title": "Commentaires", "value": total_reviews},
        {"title": "Végétarien", "value": vegetarian_friendly_count},
        {"title": "Vegan", "value": vegan_options_count},
        {"title": "Sans gluten", "value": gluten_free_count}
    ]
    return JsonResponse(summary_data, safe=False)

# Graphs 
def plotly_histogram(request):
    df = data_frame.copy()
    country_counts = df['country'].value_counts()

    fig = px.bar(country_counts, x=country_counts.index, y=country_counts.values, labels={'country':'Pays', 'y': 'Restaurants'})
    fig.update_layout(title_text='Nombre de restaurants par pays', xaxis_tickangle=-45)

    # Convert the figure to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON, 
        "title": "Nombre de restaurants par pays",
        "content": """
            Nombre de restaurants par pays 
        """
        })

# Thomas 
def diet_adaptation(request):  
    df = data_frame.copy()
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].replace({'Y': True, 'N': False})

    df['vegan_gluten_free'] = (df['vegan_options'] == True) & (df['gluten_free'] == True)
    df['vegetarian_gluten_free'] = (df['vegetarian_friendly'] == True) & (df['gluten_free'] == True)
    df['vegan_vegetarian'] = (df['vegan_options'] == True) & (df['vegetarian_friendly'] == True)
    df['vegan_gluten_free_vegetarian'] = (df['vegan_options'] == True) & (df['gluten_free'] == True) & (df['vegetarian_friendly'] == True)

    df[['vegetarian_friendly', 'vegan_options', 'gluten_free', 'vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free','vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian']].astype(int)

    df_grouped = df.groupby('country')[['vegetarian_friendly', 'vegan_options', 'gluten_free', 'vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian']].sum().reset_index()

    fig = px.bar(df_grouped, x='country', y=['vegetarian_friendly', 'vegan_options', 'gluten_free', 'vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian'],
            labels={'country':'Pays', 'vegetarian_friendly':'Options Végétariennes', 'vegan_options':'Options Véganes', 'gluten_free':'Options sans gluten', 'vegan_gluten_free':'Options vegan et sans gluten','vegetarian_gluten_free':'Options vegetarienne et sans gluten', 'vegan_vegetarian':'Options vegan et vegetarienne','vegan_gluten_free_vegetarian':'Options vegan, vegetarienne et sans gluten', 'value': 'Nombre de Restaurants' },
            title='Adaptations Diététiques dans les Restaurants par Pays')

    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                showlegend=True, xaxis_tickangle=-45)

    diet_adaptation = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return JsonResponse({
        "data": diet_adaptation, 
        "title": "Adaptations Diététiques dans les Restaurants par Pays",
        "content": """
            Dans cette dataviz, on remarque la dominance de 3 pays dans lesquels les restaurants proposent des adaptations diététiques, L’Angleterre, l’Italie et l’Espagne.
            L'Italie, l’Angleterre et l’Espagne sont les pays disposant du plus grand nombre de restaurant ayant des options végétariennes. En effet, leurs populations font partie de celle comptant le plus de végétarien en Europe (+ de 10%). On peut donc supposer que ces trois pays ont une culture culinaire contenant plus de plat végétarien que la normale comme les tapas végétariens en Espagne.
            On remarque aussi qu'ils sont ceux ayant le plus de restaurant proposant plusieurs options. Par exemple l’Angleterre est le pays ayant le plus de restaurant proposant à la fois des options végan mais aussi des options végétariennes suivi de l'Italie et de l’Espagne. On peut expliquer la forte présence de restaurant ayant des adaptations diététiques par le tourisme qui y est présent.
            On remarque de plus dans le graphe que dans tous les pays, l'adaptation diététiques la plus présente est l'option végétarienne. 5% de la population mondiale étant végétarienne les restaurants dans les zones de tourisme se doivent de proposer au moins 1 plat végétarien pour ne pas perdre de clientèle.
            Pour finir on remarque que les pays dont les restaurants propose le moins d'adaptation diététiques sont les pays dont la culture culinaire est très fortement basée sur la viande comme le Portugal ou la Bulgarie.

        """
        })

def popularity_diet(request):
    df = data_frame.copy()
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].replace({'Y': True, 'N': False})
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].astype(int)
    df['total_adaptations'] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].sum(axis=1)

    fig = px.scatter(df, x='total_reviews_count', y='total_adaptations', color='avg_rating', title='Corrélation entre Popularité et adaptation diététique')
    fig.update_layout(
        xaxis_title='Nombre d\'Avis',
        yaxis_title='Nombre d\'adaptation'
    )
    popularity_diet = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return JsonResponse({
        "data": popularity_diet, 
        "title": "Corrélation entre Popularité et adaptation diététique",
        "content": """
            Nous nous sommes demander avant la création du dataviz s’il était possible de corréler la popularité d’un restaurant avec le nombre d’adaptation diététique que celui-ci proposait. Nous retrouvons ainsi dans cette dataviz le nombre total d’adaptation proposé par un restaurant fonction du nombre d’avis que celui-ci a reçu. Chaque point représente ainsi un restaurant et la couleur de celui-ci représente la note moyenne sur tripadvisor.
            On remarque ici que peu importe le nombre de d’adaptation diététique, il n’y a pas d’incidence sur la note moyenne des restaurants en effet, les points représentant les restaurants sont plus ou moins répartis équitablement peut importe le nombre d’adaptation diététique. On remarque de plus que les notes de ces restaurant n’est pas influé par le nombre d’adaptation diététique et ce peu importe le nombre d’avis dans chaque restaurant. On peut donc dire qu’il n’y a pas de corrélation entre le nombre d’adaptation diététique et la popularité du restaurant.

        """
        })

def distrib_restaurant_regimes(request):
    df= data_frame.copy()
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].replace({'Y': True, 'N': False})
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].astype(int)
    df['total_adaptations'] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].sum(axis=1)
    grouped_df = df.groupby('country').agg({'total_adaptations': 'mean', 'latitude': 'first', 'longitude': 'first', 'restaurant_link': 'size'}).reset_index()
    
    fig = px.scatter_geo(grouped_df, 
                    lat='latitude', 
                    lon='longitude',  
                    color='total_adaptations',
                    size='restaurant_link',
                    scope='europe',
                    hover_name='country')
    fig.update_geos(
        visible=False, resolution=50, scope="europe",
        showcountries=True, countrycolor="Black",
        showsubunits=True, subunitcolor="Blue"
    )
    fig.update_layout(title_text='Distribution des restaurants spécifiques aux régimes')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return JsonResponse({
        "data": graphJSON, 
        "title": "Distribution des restaurants spécifiques aux régimes",
        "content": "Number of Restaurants per Country"
        })

# Bakari 
def plotly_bar_chart(request):
    df = data_frame.copy()
    # Compter le nombre de restaurants pour chaque type de cuisine
    france_df = df[df['country'] == 'France']
    cuisine_counts = france_df['cuisines'].value_counts().nlargest(10)

    # Filtrer le DataFrame pour inclure seulement les 10 types de cuisine les plus fréquents
    filtered_df = df[df['cuisines'].isin(cuisine_counts.index)]

    # Grouper les données filtrées par type de cuisine
    grouped_data = filtered_df.groupby('cuisines').agg({
        'value': 'mean',  # Moyenne du rapport qualité-prix
        'avg_rating': 'mean'  # Moyenne de la note moyenne
    }).reset_index()

    # Trier les types de cuisine par nombre de restaurants (dans l'ordre décroissant)
    #grouped_data = grouped_data.set_index('cuisines').loc[cuisine_counts.index].reset_index()
    grouped_data = grouped_data.sort_values(by='avg_rating', ascending=False)

    # Créer un graphique en barres avec un filtre de couleur basé sur la note moyenne
    fig = px.bar(grouped_data, x='cuisines', y='value', color='avg_rating',
                title='Rapport Qualité-Prix des 10 Types de Cuisine les Plus Fréquents en France',
                labels={'cuisines' : 'Type de cuisine', 'value': 'Rapport Qualité-Prix moyen', 'avg_rating': 'Note Moyenne'})

    # Convertir le graphique en JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON,
        "title": "Rapport Qualité-Prix des 10 Types de Cuisine les Plus Fréquents en France",
        "content": "Number of Restaurants per Country"
        })

def box_plot_service(request):
    df = data_frame.copy()
    # Utilisation de df au lieu de df
    melted_df = pd.melt(df, id_vars=['price_level'], value_vars=['service'],
                        var_name='Niveau de Satisfaction', value_name='Note')

    # Définir un dictionnaire pour la correspondance des couleurs
    colors = {'service': 'red'}  

    # Création du diagramme en boîte
    fig = px.box(melted_df, x='price_level', y='Note', color='Niveau de Satisfaction',
                title='Qualité de service par niveau de prix',
                color_discrete_map=colors)

    # Personnalisation de l'apparence du graphique
    fig.update_layout(
        xaxis_title='Niveau de Prix',
        yaxis_title='Note de Satisfaction',
        boxgap=0.2,
        boxgroupgap=0.3
    )

    # Convertir le graphique en JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON, 
        "title": "Distribution des Niveaux de Satisfaction par Niveau de Prix",
        "content": "Number of Restaurants per Country"
        })

def box_plot_value(request):
    df = data_frame.copy()
    # Utilisation de data_frame.copy() au lieu de df
    melted_df = pd.melt(df, id_vars=['price_level'], value_vars=['value'],
                        var_name='Niveau de Satisfaction', value_name='Note')

    # Définir un dictionnaire pour la correspondance des couleurs
    colors = {'value': 'green'} 

    # Création du diagramme en boîte
    fig = px.box(melted_df, x='price_level', y='Note', color='Niveau de Satisfaction',
                title='Rapport qualité-prix par niveau de prix',
                color_discrete_map=colors)

    # Personnalisation de l'apparence du graphique
    fig.update_layout(
        xaxis_title='Niveau de Prix',
        yaxis_title='Note de Satisfaction',
        boxgap=0.2,
        boxgroupgap=0.3
    )
    # Convertir le graphique en JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON, 
        "title": "Rapport qualité-prix par niveau de prix",
        "content": "Number of Restaurants per Country"
        })

def box_plot_atmosphere(request):
    df = data_frame.copy()
    # Utilisation de data_frame.copy() au lieu de df
    melted_df = pd.melt(df, id_vars=['price_level'], value_vars=['atmosphere'],
                        var_name='Niveau de Satisfaction', value_name='Note')

    # Définir un dictionnaire pour la correspondance des couleurs
    colors = {'atmosphere': 'blue'}  # Exemple : 'blue' pour 'service'

    # Création du diagramme en boîte
    fig = px.box(melted_df, x='price_level', y='Note', color='Niveau de Satisfaction',
                title='Ambiance par niveau de prix',
                color_discrete_map=colors)

    # Personnalisation de l'apparence du graphique
    fig.update_layout(
        xaxis_title='Niveau de Prix',
        yaxis_title='Note de Satisfaction',
        boxgap=0.2,
        boxgroupgap=0.3
    )

    # Convertir le graphique en JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON, 
        "title": "Evalutation de l'ambiance par niveau de prix",
        "content": "Number of Restaurants per Country"
        })

# Kemo 

def noteMoyenneNbreRestau(request): 
    df = data_frame.copy()
    # adding manually the country code - required for the geographical mapping with plotly
    countries_dict = {'Austria': 'AUT', 'Belgium': 'BEL', 'Bulgaria': 'BGR', 'Croatia': 'HRV', 'Czech Republic': 'CZE',
                    'Denmark': 'DNK', 'England': 'GBR', 'Finland': 'FIN', 'France': 'FRA', 'Germany': 'DEU',
                    'Greece': 'GRC', 'Hungary': 'HUN', 'Ireland': 'IRL', 'Italy': 'ITA', 'Northern Ireland': 'GBR',
                    'Poland': 'POL', 'Portugal': 'PRT', 'Romania': 'ROU', 'Scotland': 'GBR', 'Slovakia': 'SVK',
                    'Spain': 'ESP', 'Sweden': 'SWE', 'The Netherlands': 'NLD', 'Wales': 'GBR'}
    df['country_code'] = df['country'].map(countries_dict).fillna(df['country'])

    # average price in euro
    df['minimum_range'] = pd.to_numeric(df['price_range'].to_string().split('-')[0].replace('€', '').replace(',', ''), errors='coerce')
    df['maximum_range'] = pd.to_numeric(df['price_range'].to_string().split('-')[1].replace('€', '').replace(',', ''), errors='coerce')
    df['avg_price'] = (df['minimum_range'] + df['maximum_range'])/2

    # aggregating the data to find insights from the TripAdvisor dataset
    agg_countries_df = df.groupby('country').agg(
        total_restaurants=pd.NamedAgg(column='restaurant_link', aggfunc=np.size),
        mean_rating=pd.NamedAgg(column='avg_rating', aggfunc=np.mean),
        mean_food=pd.NamedAgg(column='food', aggfunc=np.mean),
        mean_service=pd.NamedAgg(column='service', aggfunc=np.mean),
        mean_values=pd.NamedAgg(column='value', aggfunc=np.mean),
        mean_athmosphere=pd.NamedAgg(column='atmosphere', aggfunc=np.mean),
        total_reviews=pd.NamedAgg(column='total_reviews_count', aggfunc=np.sum),
        mean_reviews_n=pd.NamedAgg(column='total_reviews_count', aggfunc=np.mean),
        median_reviews_n=pd.NamedAgg(column='total_reviews_count', aggfunc=np.median),
        mean_price=pd.NamedAgg(column='avg_price', aggfunc=np.mean),
        median_price=pd.NamedAgg(column='avg_price', aggfunc=np.median),
        open_days_per_week=pd.NamedAgg(column='open_days_per_week', aggfunc=np.mean),
        open_hours_per_week=pd.NamedAgg(column='open_hours_per_week', aggfunc=np.mean),
        working_shifts_per_week=pd.NamedAgg(column='working_shifts_per_week', aggfunc=np.mean)
    ).reset_index(level=0).sort_values(by='total_restaurants', ascending=False)
    for col in agg_countries_df.columns[1:]:
        agg_countries_df[col] = round(agg_countries_df[col], 3)
    agg_countries_df['country_code'] = agg_countries_df['country'].map(countries_dict).fillna(agg_countries_df['country'])

    # Bubble plot with the relationship between total_votes and avg_vote for the European countries
    fig = go.Figure(data=go.Scatter(x=agg_countries_df['total_restaurants'], y=agg_countries_df['mean_rating'],
    mode='markers+text', marker=dict(size=(agg_countries_df['median_reviews_n'].astype('float64')*0.09),
                                    color=agg_countries_df['median_reviews_n']),
    text=agg_countries_df['country'], textposition='top center', textfont=dict(size=9),
    customdata=agg_countries_df['median_reviews_n'],
    hoverlabel=dict(namelength=0), # removes the trace number off to the side of the tooltip box
    hovertemplate='<b>%{text}</b>:<br>%{x:,} total restaurants<br>%{y:.2f} mean rating<br>%{customdata} median revies'))
    
    fig.update_layout(title='Note moyenne et nombre total de restaurants dans les 20 premières villes européennes (taille en fonction de la médiane)', template='plotly_white',
                    title_x=0.5, legend=dict(yanchor='bottom', y=-0.15, xanchor='left', x=0, font=dict(size=10), orientation='h'),
                    autosize=True)
    fig['layout']['xaxis']['title'] = 'Total Restaurants'
    fig['layout']['yaxis']['title'] = 'Note Moyenne'

    # Convertir le graphique en JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON, 
        "title": "Note moyenne et nombre total de restaurants dans les 20 premières villes européennes (taille en fonction de la médiane)",
        "content": "Number of Restaurants per Country"
    })

def round_decimals_up_or_down(direction:str, number:float, decimals:int=2):
    if not isinstance(decimals, int):
        raise TypeError('decimal places must be an integer')
    elif decimals < 0:
        raise ValueError('decimal places has to be 0 or more')
    elif decimals == 0:
        if direction == 'up':
            return math.ceil(number)
        elif direction == 'down':
            return math.floor(number)
        else:
            raise ValueError('direction needs to be up or down')
    factor = 10 ** decimals
    if direction == 'up':
        return math.ceil(number * factor) / factor
    elif direction == 'down':
        return math.floor(number * factor) / factor
    else:
        raise ValueError('direction needs to be up or down')

def radar_chart(request):
    df = data_frame.copy()
    # Compter le nombre de restaurants par pays
    restaurant_counts = df['country'].value_counts()

    # Sélectionner les 8 pays ayant le plus grand nombre de restaurants
    top8_countries = restaurant_counts.nlargest(8).index

    country_agg_cols_dict = {
        'country': 'Country',
        'avg_rating': 'Rating',
        'food': 'Food',
        'service': 'Service',
        'value': 'Value',
        'atmosphere': 'Athmosphere'
    }
    top8_countries_df = df[df['country'].isin(top8_countries)]
    top8_countries_df = top8_countries_df[list(country_agg_cols_dict.keys())]
    top8_countries_df.rename(columns=country_agg_cols_dict, inplace=True)
    # melting the various categories, so that the line_polar graph can be easily called
    top8_countries_df = top8_countries_df.melt(id_vars=['Country'],
                                            value_vars=['Rating', 'Food', 'Service', 'Value', 'Athmosphere'],
                                            var_name='Category', 
                                            value_name='AggValue'
                                        )
    top8_countries_df['AggValue'] = round(top8_countries_df['AggValue'], 3)

    decimal_val = 1
    max_countries_val = round_decimals_up_or_down(direction='up', number=top8_countries_df['AggValue'].max(), decimals=decimal_val)
    min_countries_val = round_decimals_up_or_down(direction='down', number=top8_countries_df['AggValue'].min(), decimals=decimal_val)

    # radar plot with plotly
    fig = px.line_polar(top8_countries_df, r='AggValue', range_r=[min_countries_val, max_countries_val], theta='Category', color='Country', line_close=True, template='seaborn')
    fig.update_layout(title_text='Notes Globales du top 8', title_x=0.5, title_y=0.97, margin=dict(l=80, r=10, t=40, b=10))

    # Convertir le graphique en JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON, 
        "title": "Notes Globales du top 8",
        "content": "Number of Restaurants per Country"
    })

