from django.apps import AppConfig
from .data import load_data 

class BackendAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend_app'

    def ready(self):
        load_data.load_csv_data()  # Call your function
