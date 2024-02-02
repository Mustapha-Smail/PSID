# load_data.py
from django.conf import settings
import pandas as pd

def load_csv_data():
    # global data_frame
    file = settings.CSV_FILE
    data_frame = pd.read_csv(file)

    data_frame.dropna(
        subset = ["restaurant_name", "country", "price_level", "meals", "cuisines", "vegetarian_friendly", "vegan_options", "gluten_free", "avg_rating", "service", "value", "atmosphere"], 
        inplace=True
    )
    data_frame['cuisines'] = data_frame['cuisines'].str.split(',').str[0]
    
    return data_frame
