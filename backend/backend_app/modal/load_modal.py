from ..globals import DATA_FRAME
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd 

BINARY_ENCODER = preprocessing.LabelBinarizer()
LABEL_ENCODER = preprocessing.LabelEncoder()

def train_model(): 
    # Nettoyage de données 
    # Data cleaning
    original_data = DATA_FRAME.copy()
    data = original_data.dropna(subset=['region']).copy()  # A better approach to dropna based on 'region'
    data = data[['restaurant_link', 'price_level', 'vegetarian_friendly', 'vegan_options', 'gluten_free', 'avg_rating']]

    # Data encoding
    data['vegetarian_friendly'] = BINARY_ENCODER.fit_transform(data['vegetarian_friendly'])
    data['vegan_options'] = BINARY_ENCODER.fit_transform(data['vegan_options'])
    data['gluten_free'] = BINARY_ENCODER.fit_transform(data['gluten_free'])

    data['price_level'] = LABEL_ENCODER.fit_transform(data['price_level'])

    # Splitting the dataset
    X_train, X_test = train_test_split(data, test_size=0.2, random_state=42)

    # Training a KMeans cluster with a specified number of clusters
    kmeans = KMeans(n_clusters=15, n_init=10, random_state=0)
    kmeans.fit(X_train.iloc[:, 1:])  # Fitting on features, excluding 'restaurant_link'

    # Assigning cluster labels to the training data
    X_train['cluster'] = kmeans.labels_

    # Merging the original data with the new 'cluster' column
    data_trained = pd.merge(original_data, X_train[['restaurant_link', 'cluster']], on='restaurant_link', how='left')

    # Return both the modified DataFrame and the KMeans model
    return data_trained, kmeans

def predict_user_cluster(preferences):

    trained_data, kmeans_model = train_model()

    # Step 2: Preprocess the Preference Data
    preferences['vegetarian_friendly'] = BINARY_ENCODER.transform(preferences['vegetarian_friendly'])
    preferences['vegan_options'] = BINARY_ENCODER.transform(preferences['vegan_options'])
    preferences['gluten_free'] = BINARY_ENCODER.transform(preferences['gluten_free'])
    preferences['price_level'] = LABEL_ENCODER.transform(preferences['price_level'])
    
    # Step 3: Predict the cluster for the user's preferences
    predicted_cluster = kmeans_model.predict(preferences)
    
    # Step 4: Filter the trained_data to get restaurants in the predicted cluster
    recommended_restaurants = trained_data[trained_data['cluster'] == predicted_cluster[0]]

    recommended_restaurants = recommended_restaurants[['id', 'restaurant_link', 'restaurant_name', 'address', 'avg_rating']]
    
    return recommended_restaurants
