from app.views.main_view import render_app
from app.models.data_loader import load_all_data
from app.models.data_transformation import preprocess_truck_traffic_with_regions, preprocess_edges_with_coordinates


def main():
    
    # Load all data and cache it
    load_all_data()

    # Do the necessary transformations

    # create the truck traffic with regions dataset and cache it inside the _cached_transformed_data dictionary
    preprocess_truck_traffic_with_regions()

    # create the edges with coordinates dataset and cache it inside the _cached_transformed_data dictionary
    preprocess_edges_with_coordinates()

    # Render the Streamlit app
    render_app()



if __name__ == "__main__":
    main()

