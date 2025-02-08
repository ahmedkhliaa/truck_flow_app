import streamlit as st
from app.views.country_selection import render_country_selection
from app.views.region_selection import render_region_selection
from app.views.year_selector import render_year_selector
from app.controllers.journey_controller import filter_journeys_by_countries, select_journeys
from app.controllers.route_preparation import prepare_routes
from app.controllers.user_input_controller import handle_user_input
from app.views.route_display import display_routes
from app.models.data_transformation import _cached_transformed_data

def render_app():
    """
    Main function to render the Streamlit app.
    """
    st.title("Transport Flow Visualization App")

    # Access cached transformed data
    edges_with_coordinates = _cached_transformed_data.get("edges_with_coordinates")
    truck_with_regions = _cached_transformed_data.get("truck_with_regions")

    if edges_with_coordinates.empty or truck_with_regions.empty:
        st.error("Data has not been preprocessed correctly. Please check your app setup.")
        return

    # Render country selection UI
    origin_countries, destination_countries = render_country_selection()

    # Transform country names to country codes
    origin_codes, destination_codes = handle_user_input(origin_countries, destination_countries)

    if origin_countries and destination_countries:
        # Filter journeys by countries
        filtered_journeys = filter_journeys_by_countries(origin_codes, destination_codes)
        st.write("Filtered Journeys:", filtered_journeys)

        if not filtered_journeys.empty:
            # Render year selector
            selected_year = render_year_selector()

            # Render region selection
            origin_regions, destination_regions = render_region_selection(filtered_journeys)

            # Select specific journeys
            selected_journeys = select_journeys(origin_regions, destination_regions, filtered_journeys)
            st.write("Selected Journey:", selected_journeys)

            # Prepare routes for visualization
            route_data = prepare_routes(selected_journeys, edges_with_coordinates)
            st.write(f"The route to be displayed:",route_data)


            # Display routes on the map
            display_routes(route_data, selected_year)
        else:
            st.warning("No journeys found for the selected countries. Please try again.")

