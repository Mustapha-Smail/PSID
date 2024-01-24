# load_data.py
from django.conf import settings
import pandas as pd

def load_csv_data():
    global data_frame
    file = settings.CSV_FILE
    data_frame = pd.read_csv(file)
    # Perform any additional data processing here if needed
    data_frame = data_frame[["restaurant_name", "country", "top_tags", "price_level", "meals", "cuisines", "vegetarian_friendly", "vegan_options", "gluten_free", "open_hours_per_week", "avg_rating", "total_reviews_count", "service", "value", "atmosphere", "special_diets", "latitude", "longitude", "restaurant_link"]]
    data_frame = data_frame.dropna()
    data_frame['cuisines'] = data_frame['cuisines'].str.split(',').str[0]
