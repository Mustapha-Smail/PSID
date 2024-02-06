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
    data = original_data.dropna(
        subset=["region"]
    ).copy()  # A better approach to dropna based on 'region'
    data = data[
        [
            "restaurant_link",
            "region",
            "price_level",
            "vegetarian_friendly",
            "vegan_options",
            "gluten_free",
            "avg_rating",
        ]
    ]

    # Data encoding
    data["vegetarian_friendly"] = BINARY_ENCODER.fit_transform(
        data["vegetarian_friendly"]
    )
    data["vegan_options"] = BINARY_ENCODER.fit_transform(data["vegan_options"])
    data["gluten_free"] = BINARY_ENCODER.fit_transform(data["gluten_free"])

    data["price_level"] = LABEL_ENCODER.fit_transform(data["price_level"])

    # Splitting the dataset
    X_train, X_test = train_test_split(data, test_size=0.2, random_state=42)

    # Training a KMeans cluster with a specified number of clusters
    kmeans = KMeans(n_clusters=15, n_init=10, random_state=0)
    kmeans.fit(X_train.iloc[:, 2:])  # Fitting on features, excluding 'restaurant_link'

    # Assigning cluster labels to the training data
    X_train["cluster"] = kmeans.labels_

    # Merging the original data with the new 'cluster' column
    data_trained = pd.merge(
        original_data,
        X_train[["restaurant_link", "cluster"]],
        on="restaurant_link",
        how="left",
    )

    # Return both the modified DataFrame and the KMeans model
    return data_trained, kmeans


def predict_user_cluster(preferences):

    trained_data, kmeans_model = train_model()

    # Step 1: Preprocess the Preference Data (excluding 'region' for KMeans prediction)
    preferences_for_kmeans = (
        preferences.copy()
    )  # Create a copy to avoid altering the original preferences
    preferences_for_kmeans["vegetarian_friendly"] = BINARY_ENCODER.transform(
        preferences_for_kmeans[["vegetarian_friendly"]]
    )
    preferences_for_kmeans["vegan_options"] = BINARY_ENCODER.transform(
        preferences_for_kmeans[["vegan_options"]]
    )
    preferences_for_kmeans["gluten_free"] = BINARY_ENCODER.transform(
        preferences_for_kmeans[["gluten_free"]]
    )
    preferences_for_kmeans["price_level"] = LABEL_ENCODER.transform(
        preferences_for_kmeans[["price_level"]]
    )

    # Remove 'region' from the DataFrame used for KMeans prediction
    features_for_kmeans = preferences_for_kmeans.drop(
        columns=["region"], errors="ignore"
    )

    # Step 2: Filter the Trained Data by the Specified Region
    if "region" in preferences:
        region = preferences["region"].iloc[0]  # Extracting the region value
        data_within_region = trained_data[trained_data["region"] == region]
    else:
        data_within_region = trained_data

    # Predict the cluster for the filtered data
    # Since KMeans doesn't inherently filter by region, predictions are made on the region-filtered data
    predicted_cluster = kmeans_model.predict(features_for_kmeans)

    # Step 3: Filter Recommendations Within the Predicted Cluster
    recommended_restaurants = data_within_region[
        data_within_region["cluster"] == predicted_cluster[0]
    ]

    # Select desired columns for the output
    recommended_restaurants = recommended_restaurants[
        ["id", "restaurant_link", "restaurant_name", "address", "avg_rating"]
    ]

    return recommended_restaurants
