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
            L'Italie possède le plus grand nombre de restaurants parmi les pays listés, suivi de la France et de l'Espagne. Les autres pays ont significativement moins de restaurants comparés à ces trois premiers, avec des nombres qui diminuent progressivement. Les pays comme le Danemark, la République Tchèque, la Hongrie, la Pologne, la Roumanie, la Finlande, la Bulgarie et la Slovaquie ont les nombres les plus faibles dans cet ensemble de données.
            <br>
            On remarque que l'Italie, la France et l'Espagne pourraient être des destinations populaires pour la gastronomie ou que ces pays ont une culture de la restauration plus prononcée. Cela pourrait aussi refléter des facteurs socio-économiques, touristiques ou démographiques qui influencent le nombre de restaurants. 
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
            Dans cette dataviz, on remarque la dominance de 3 pays dans lesquels les restaurants proposent des adaptations diététiques, L’Angleterre, l’Italie et l’Espagne.<br>
            L'Italie, l’Angleterre et l’Espagne sont les pays disposant du plus grand nombre de restaurant ayant des options végétariennes. En effet, leurs populations font partie de celle comptant le plus de végétariens en Europe (+ de 10%). On peut donc supposer que ces trois pays ont une culture culinaire contenant plus de plats végétariens que la normale comme les tapas végétariens en Espagne.<br>
            On remarque aussi qu'ils sont ceux ayant le plus de restaurants proposant plusieurs options. Par exemple, l’Angleterre est le pays ayant le plus de restaurants proposant à la fois des options végan mais aussi des options végétariennes suivi de l'Italie et de l’Espagne. On peut expliquer la forte présence de restaurant ayant des adaptations diététiques par le tourisme qui y est présent.<br>
            On remarque de plus dans le graphe que dans tous les pays, l'adaptation diététique la plus présente est l'option végétarienne. 5% de la population mondiale étant végétarienne, les restaurants dans les zones de tourisme se doivent de proposer au moins un plat végétarien pour ne pas perdre de clientèle.<br>
            Pour finir on remarque que les pays dont les restaurants propose le moins d'adaptations diététiques sont les pays dont la culture culinaire est très fortement basée sur la viande comme le Portugal ou la Bulgarie.

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
            On remarque ici que peu importe le nombre de d’adaptation diététique, il n’y a pas d’incidence sur la note moyenne des restaurants en effet, les points représentant les restaurants sont plus ou moins répartis équitablement peu importe le nombre d’adaptations diététiques. On remarque de plus, que les notes de ces restaurants ne sont pas influncés par le nombre d’adaptations diététiques, et ce, peu importe le nombre d’avis dans chaque restaurant. On peut donc dire qu’il n’y a pas de corrélation entre le nombre d’adaptations diététiques et la popularité du restaurant.

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
        "content": """
        Cette dataviz est une carte représentant la moyenne d’adaptation par restaurant dans les pays d’Europe. Ici chaque point représente un pays, sa couleur représente la moyenne des adaptations des restaurants par pays et la taille correspond au nombre de restaurant par pays.<br>
        On remarque ici que les pays qui possédaient le plus de restaurant proposant des adaptations diététiques n’en ont pas une proportion si élevée par rapport au nombre total de restaurant dans le pays, Par exemple l’Italie et l’Espagne qui possédaient le plus de restaurant ayant des adaptations diététiques font finalement partie des pays ayant la plus petite part de restaurant ayant des adaptations diététiques. <br>
        Dans le même temps on remarque que l’Angleterre reste parmi les pays ayant en moyenne le plus d’adaptation diététique dans leur restaurant avec la Grèce ce qui peut être expliquer par leur forte utilisation de fruit et de légume dans leurs plats.<br>
        La France au contraire qui était un des pays avec le plus d’adaptation diététiques est finalement un des pays ayant un faible part d’adaptation diététique dans ces restaurants.
        """
        })

# Bakari 
def plotly_bar_chart(request):
    df = data_frame.copy()
    # Compter le nombre de restaurants par pays
    restaurant_counts = df['country'].value_counts()
    # Sélectionner les 8 pays ayant le plus grand nombre de restaurants
    top8_countries = restaurant_counts.nlargest(8).index
    # Compter le nombre de restaurants pour chaque type de cuisine
    france_df = df[df['country'].isin(top8_countries)]
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
                title='Rapport Qualité-Prix des 10 Types de Cuisines principales sur du Top 8',
                labels={'cuisines' : 'Type de cuisine', 'value': 'Rapport Qualité-Prix moyen', 'avg_rating': 'Note Moyenne'})

    # Convertir le graphique en JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return JsonResponse({
        "data": graphJSON,
        "title": "Rapport Qualité-Prix des 10 Types de Cuisine sur le Top 8",
        "content": """
        Cette visualisation représente les 10 types de restaurants (cuisines) les plus répandus au sein des 8 pays où l’on trouve le plus de restaurants en Europe. <br>
        Sur l’axe des abscisses se trouvent les types de cuisines, sur l’axe des ordonnées le rapport qualité-prix moyen (Hauteur des barres, allant de 0 à 5) et le dégradée de couleur représente la note moyenne de chacun de ses types de cuisine. <br>
        On observe que les restaurants bars sont ceux qui ont le rapport qualité-prix moyen le plus haut et la note moyenne la plus. Les restaurants chinois bien que relativement appréciés, pour leur rapport qualité-prix, sont ceux qui ont les notes globales les plus basses. <br>
        Globalement le rapport qualité prix moyen des restaurants les plus populaires dans les pays contenant le plus de restaurant en Europe est similaire, les valeurs sont regroupées autour de la note 4. De plus il semble y avoir une corrélation claire entre la note générale, et la note évaluant le rapport qualité-prix d’un restaurant. 
        """
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
        "content": """
        (Notée de 1 à 5, par pas de 0,5) <br><br>
        Ce graphique représente les distributions de qualité de service par rapport aux niveaux de prix. <br>
        La qualité de service a une médiane similaire pour les trois niveaux de prix, se situant autour de 4 sur une échelle de 5 mais est légèrement plus élevée pour les niveaux de prix (€€€€). La variabilité de la qualité de service (représentée par la hauteur de la boîte et la longueur des moustaches) semble être similaire pour les catégories de prix les plus élevées (€€€€ et €€-€€€), tandis que la catégorie de prix la plus basse (€) semble avoir une variabilité légèrement plus faible. <br>
        Cela suggère que les restaurants les moins chères ont des qualités de service similaires. Il existe des valeurs aberrantes dans les trois catégories, indiquant des cas où la qualité de service était nettement inférieure à la médiane.<br>
        Il est intéressant de noter que le niveau de service perçu ne semble pas augmenter de façon drastique avec le niveau de prix, suggérant que payer plus cher ne garantit pas nécessairement une meilleure qualité de service selon notre jeu de données.

        """
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
        "content": """
        (Notée de 1 à 5, par pas de 0,5) <br><br>
        Ce graphique représente les distributions de rapport qualité-service des restaurants par rapport aux niveaux de prix. <br>
        On constate que la ligne médiane, qui coupe la boîte en son centre, indique une valeur médiane assez proche entre les trois catégories de prix. Cela suggère que la perception du rapport qualité-prix reste relativement stable quel que soit le montant dépensé. <br>
        Les boîtes sont équivalentes entre pour les niveaux de prix les plus élevés (€€€€) et les niveaux de prix moyens (€€-€€€). Cependant, la position de la boite est plus haute de 0,5 point pour les restaurants ayant les niveaux de prix les plus faibles (€). Ce qui indique comme nous aurions pu nous y attendre, que les niveaux de satisfaction sont plus élevés pour ceux-ci. <br>
        Enfin, les valeurs aberrantes, représentées par les points situés en dehors des moustaches, mettent en lumière des cas où le rapport qualité-prix a été jugé nettement insatisfaisant, malgré un nombre limité de ces occurrences dans les catégories de prix les moins chères et moyennes.
        """
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
        "content": """
        (Notée de 1 à 5, par pas de 0,5) <br><br>
        Ce graphique représente les distributions de qualité de l’atmosphère (ambiance) par rapport aux niveaux de prix. <br>
        L'atmosphère, tout comme les précédentes mesures de qualité de service et de rapport qualité-prix, est évaluée sur une échelle de 1 à 5. La médiane, contrairement à ce que l’on pouvait s’y attendre est la même dans tous les restaurants. Elle, est constante à travers les autres niveaux de prix. <br>
        Les quartiles, qui déterminent la hauteur de chaque boîte, montrent une variabilité plus importante pour le niveau de prix moyens (€€-€€€), ce qui indique une plus grande diversité dans les opinions sur l'atmosphère et la qualité de l’ambiance perçue. <br>
        Les valeurs aberrantes se situent bien en dessous de la médiane pour les catégories de prix élevées (€€€€), montrant que certains clients ont évalué l'atmosphère de manière beaucoup plus négative par rapport aux autres et que du fait du prix s’attendent à une expérience plus qualitative. <br>
        Globalement, cette visualisation suggère que, bien que l'atmosphère soit en général jugée de manière stable à travers les différentes gammes de prix, il existe des expériences nettement insatisfaisantes, surtout dans les établissements moins chers et ceux de gamme moyenne. 
        """
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
        "content": """
        Nous avons un graphique, un nuage de point, représentant le nombre total de restaurants dans un pays donnée en faisant la relation avec la note moyenne des restaurants dans 20 pays européens. Les pays sont espacés le long de l'axe des abscisses en fonction du nombre de restaurants présents sur leur sol. Les notes semblent varient entre  3,8 et 4,2 (approximativement), ce qui nous laiss penser que la qualité des restaurants est globalement élevée dans l'ensemble. La taille des points, dans le nuage, représentent la médiane des notes. <br> <br>
        Il y a une concentration notable de pays avec un nombre plus restreint de restaurants affichant des notes moyennes légèrement supérieures. Cette tendance est visible par les nombreux points regroupés dans la partie supérieure gauche du graphique, indiquant que des pays moins saturées en termes de nombre de restaurants pourraient offrir une qualité globalement meilleure.<br>
        Les pays qui se caractérisent par un grand nombre de restaurants, maintiennent des notes moyennes autour ou légèrement au-dessus de la moyenne. Cela suggère que, malgré une grande quantité d'offres, ces marchés parviennent à conserver un niveau de qualité satisfaisant. <br>
        Des pays comme la Grèce et l'Irlande, bien qu'ayant moins de restaurants, se distinguent par des notes moyennes particulièrement élevées. Cela peut être le reflet d'une qualité exceptionnelle ou d'une expérience culinaire qui répond très bien aux attentes des clients dans ces localités. <br>
        En conclusion, ce graphique indique qu'une bonne satisfaction cliente peut être atteinte même s'il existe beaucoup de restaurants, elle permet aussi de noter que les pays avec moins de restaurants présent sur leur sol, peuvent représenter des opportunités (pour des investisseurs par exemple). 
        """
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
        "content": """
            Nous avons un diagramme qui va faire une comparaison sur les notes globales de 8 pays européen en fonction de catégories qualités. On peut voir que la France affiche des résultats assez élevées de manière globale sur l'ensemble des catégories. L'Allemagne et L'Espagne montre quant à eux des résultats assez équivalentes. <br>
            Ensuite, nous pouvons observer que l'Angleterre présente des notes inférieurs, cela nous indique le niveau de la cuisine qui est proposée en Angleterre et peut présenter les axes d'améliorations pour chaque catégorie. <br>
            Enfin, la Belgique, la Grèce et le Portugal présentent des résultats qui sont assez éparpillés, dans le sens où, dans certaines catégories leur note est plutôt élévé et dans d'autres moins.  <br>

            Ce Radar chart nous permet d'avoir une vue globale sur la performance de huit pays européens dans le secteur de la restauration, en fonction de quatre catégories de qualité qui sont le Nourriture, l'Atmosphère, le Service, la Valeur et une note générale. La France et l'Italie semblent offrir les meilleures expériences en termes de Nourriture, tandis que l'Espagne offre la meilleure Valeur. L'Angleterre pourrait chercher à améliorer son offre culinaire et son atmosphère pour se rapprocher des autres pays. <br>

            Un pays avec une forme équilibrée aurait une performance plus constante à travers les catégories, tandis que des pointes indiquent des forces dans des domaines spécifiques. <br>

            On peut donc dire que, ce graphique fournit une comparaison visuelle rapide à un utilisateur quelconque, comme les professionnels de la restauration ou les organismes de tourisme ou encore un utilisateur visitant un pays, à identifier les domaines où les pays perfoment et les opportunités d'amélioration dans l'expérience culinaire qu'ils offrent. <br>
        """
    })

