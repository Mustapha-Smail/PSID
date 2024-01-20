# load_data.py
from django.conf import settings
import pandas as pd

def load_csv_data():
    global data_frame
    file = settings.CSV_FILE
    data_frame = pd.read_csv(file)
    # Perform any additional data processing here if needed