from app.models.data_loader import load_all_data
from app.models.data_transformation import preprocess_truck_traffic_with_regions, preprocess_edges_with_coordinates

def initialize_app():
    """
    Initialize the app by loading and preprocessing all required data.
    """
    print("Initializing app and loading data...")

    # Load raw data into cache
    load_all_data()

    # Preprocess required data and cache it
    preprocess_truck_traffic_with_regions()
    preprocess_edges_with_coordinates()

    print("Data initialization complete!")
