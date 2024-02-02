import pandas as pd
from backend_app.models import Restaurant, DataInsertionStatus

def load_data_db(): 
    # global data_frame

    insertion_status = DataInsertionStatus.objects.first()

    if insertion_status and insertion_status.has_data_been_inserted:
        # Query the Restaurant table and retrieve all records
        restaurant_records = Restaurant.objects.all()

        # Convert the queryset to a DataFrame
        data_frame = pd.DataFrame.from_records(restaurant_records.values())

        data_frame['latitude']=data_frame['latitude'].astype(float)
        data_frame['longitude']=data_frame['longitude'].astype(float)
        data_frame['open_days_per_week']=data_frame['open_days_per_week'].astype(float)
        data_frame['open_hours_per_week']=data_frame['open_hours_per_week'].astype(float)
        data_frame['working_shifts_per_week']=data_frame['working_shifts_per_week'].astype(float)
        data_frame['avg_rating']=data_frame['avg_rating'].astype(float)
        data_frame['total_reviews_count']=data_frame['total_reviews_count'].astype(float)
        data_frame['reviews_count_in_default_language']=data_frame['reviews_count_in_default_language'].astype(float)
        data_frame['excellent']=data_frame['excellent'].astype(float)
        data_frame['very_good']=data_frame['very_good'].astype(float)
        data_frame['average']=data_frame['average'].astype(float)
        data_frame['poor']=data_frame['poor'].astype(float)
        data_frame['terrible']=data_frame['terrible'].astype(float)
        data_frame['food']=data_frame['food'].astype(float)
        data_frame['service']=data_frame['service'].astype(float)
        data_frame['value']=data_frame['value'].astype(float)
        data_frame['atmosphere']=data_frame['atmosphere'].astype(float)

        return data_frame
