import plotly
import plotly.graph_objs as go
import plotly.express as px
import random
import json
from django.http import JsonResponse
import pandas as pd
from .data.load_data import data_frame 

def plotly_histogram(request):
    country_counts = data_frame['country'].value_counts()

    fig = px.bar(country_counts, x=country_counts.index, y=country_counts.values, labels={'x': 'Country', 'y': 'Number of Restaurants'})
    fig.update_layout(title_text='Number of Restaurants per Country', xaxis_tickangle=-45)

    # Convert the figure to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON, 
        "title": "Number of Restaurants per Country",
        "content": """
            Nombre de restaurants par pays 
        """
        })


def diet_adaptation(request):  
    df = data_frame
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].replace({'Y': True, 'N': False})

    df['vegan_gluten_free'] = (df['vegan_options'] == True) & (df['gluten_free'] == True)
    df['vegetarian_gluten_free'] = (df['vegetarian_friendly'] == True) & (df['gluten_free'] == True)
    df['vegan_vegetarian'] = (df['vegan_options'] == True) & (df['vegetarian_friendly'] == True)
    df['vegan_gluten_free_vegetarian'] = (df['vegan_options'] == True) & (df['gluten_free'] == True) & (df['vegetarian_friendly'] == True)

    df[['vegetarian_friendly', 'vegan_options', 'gluten_free', 'vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free','vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian']].astype(int)

    df_grouped = df.groupby('country')[['vegetarian_friendly', 'vegan_options', 'gluten_free', 'vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian']].sum().reset_index()

    fig = px.bar(df_grouped, x='country', y=['vegetarian_friendly', 'vegan_options', 'gluten_free', 'vegan_gluten_free', 'vegetarian_gluten_free', 'vegan_vegetarian', 'vegan_gluten_free_vegetarian'],
            labels={'country':'Pays', 'vegetarian_friendly':'Options Végétariennes', 'vegan_options':'Options Véganes', 'gluten_free':'Options sans gluten', 'vegan_gluten_free':'Options vegan et sans gluten','vegetarian_gluten_free':'Options vegetarienne et sans gluten', 'vegan_vegetarian':'Options vegan et vegetarienne','vegan_gluten_free_vegetarian':'Options vegan, vegetarienne et sans gluten' },
            title='Adaptations Diététiques dans les Restaurants par Pays')

    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
                showlegend=True)

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
    df = data_frame
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].replace({'Y': True, 'N': False})
    df[['vegetarian_friendly', 'vegan_options', 'gluten_free']] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].astype(int)
    df['total_adaptations'] = df[['vegetarian_friendly', 'vegan_options', 'gluten_free']].sum(axis=1)

    fig = px.scatter(df, x='total_reviews_count', y='total_adaptations', color='avg_rating', title='Corrélation entre Popularité et adaptation diététique')
    popularity_diet = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return JsonResponse({
        "data": popularity_diet, 
        "title": "Corrélation entre Popularité et adaptation diététique",
        "content": """
            Nous nous sommes demander avant la création du dataviz s’il était possible de corréler la popularité d’un restaurant avec le nombre d’adaptation diététique que celui-ci proposait. Nous retrouvons ainsi dans cette dataviz le nombre total d’adaptation proposé par un restaurant fonction du nombre d’avis que celui-ci a reçu. Chaque point représente ainsi un restaurant et la couleur de celui-ci représente la note moyenne sur tripadvisor.
            On remarque ici que peu importe le nombre de d’adaptation diététique, il n’y a pas d’incidence sur la note moyenne des restaurants en effet, les points représentant les restaurants sont plus ou moins répartis équitablement peut importe le nombre d’adaptation diététique. On remarque de plus que les notes de ces restaurant n’est pas influé par le nombre d’adaptation diététique et ce peu importe le nombre d’avis dans chaque restaurant. On peut donc dire qu’il n’y a pas de corrélation entre le nombre d’adaptation diététique et la popularité du restaurant.

        """
        })

def distrib_restaurant_régimes(request):
    df= data_frame
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

    fig.update_layout(title_text='Distribution des restaurants spécifiques aux régimes')
    distrib_restaurant_régimes = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return JsonResponse({
        "data": distrib_restaurant_régimes, 
        "title": "Distribution des restaurants spécifiques aux régimes",
        "content": "Number of Restaurants per Country"
        })


def plotly_bar_chart(request):
    # Compter le nombre de restaurants pour chaque type de cuisine
    france_df = data_frame[data_frame['country'] == 'France']
    cuisine_counts = france_df['cuisines'].value_counts().nlargest(10)

    # Filtrer le DataFrame pour inclure seulement les 10 types de cuisine les plus fréquents
    filtered_df = data_frame[data_frame['cuisines'].isin(cuisine_counts.index)]

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
    # Utilisation de data_frame au lieu de df
    melted_df = pd.melt(data_frame, id_vars=['price_level'], value_vars=['service'],
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
    # Utilisation de data_frame au lieu de df
    melted_df = pd.melt(data_frame, id_vars=['price_level'], value_vars=['value'],
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
    # Utilisation de data_frame au lieu de df
    melted_df = pd.melt(data_frame, id_vars=['price_level'], value_vars=['atmosphere'],
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