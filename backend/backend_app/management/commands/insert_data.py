from django.core.management.base import BaseCommand
from backend_app.models import DataInsertionStatus, Restaurant
from backend_app.data import load_data

class Command(BaseCommand):
    help = 'Insert data into the database'

    def handle(self, *args, **options):
        # Check the insertion status
        insertion_status = DataInsertionStatus.objects.first()

        if insertion_status and insertion_status.has_data_been_inserted:
            self.stdout.write(self.style.SUCCESS("Data has already been inserted."))
        else:
            # Insert your data into the database
            df_data = load_data.load_csv_data()
            # df_data = df_data[["restaurant_name", "country", "price_level", "meals", "cuisines", "vegetarian_friendly", "vegan_options", "gluten_free", "avg_rating", "service", "value", "atmosphere"]]
            # df_data = df_data.head(100)
            df_data = df_data.to_dict(orient='records')
            for data in df_data:
                instance = Restaurant(**data)
                instance.save()
            # Update the insertion status
            if not insertion_status:
                DataInsertionStatus.objects.create(has_data_been_inserted=True)
            else:
                insertion_status.has_data_been_inserted = True
                insertion_status.save()

            self.stdout.write(self.style.SUCCESS("Data inserted successfully."))
