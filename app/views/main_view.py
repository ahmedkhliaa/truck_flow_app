import streamlit as st
from app.views.country_selection import render_country_selection
from app.views.year_selector import render_year_selector
from app.views.region_selection import render_region_selection
from app.controllers.journey_controller import get_filtered_journeys_by_countries, get_filtered_journeys_by_regions
from app.controllers.user_input_controller import handle_user_input
from app.models.data_loader import load_edge_with_node_coordinates_data
from app.controllers.route_preparation import prepare_routes
from app.views.route_display import display_routes

def render_app():
    """
    Main function to render the Streamlit app.
    """
    st.title("Transport Flow Visualization App")

    # Access the edges with node coordinates data
    edges_with_node_coordinates = load_edge_with_node_coordinates_data()

    # Render country selection UI
    origin_countries, destination_countries = render_country_selection()

    # Transform country names to country codes
    origin_codes, destination_codes = handle_user_input(origin_countries, destination_countries)

    if origin_countries and destination_countries:

        # Filter Journeys by Countries
        filtered_journeys = get_filtered_journeys_by_countries(origin_codes,destination_codes)
        st.write("Filtered Journeys:", filtered_journeys)

        if not filtered_journeys.empty:

            # Render year selector
            selected_year = render_year_selector()

            # Render region selection
            origin_regions, destination_regions = render_region_selection(filtered_journeys)

            # Select specific journeys
            selected_journeys = get_filtered_journeys_by_regions(origin_regions, destination_regions)

            if selected_journeys is not None:
                st.write("Selected Journey(s):", selected_journeys)
                # Prepare routes for visualization
                route_data = prepare_routes(selected_journeys, edges_with_node_coordinates)
                st.write(f"The route to be displayed:",route_data)

                # Display routes on the map
                display_routes(route_data, selected_year)

            else:
                st.warning("No journeys found for the selected regions. Please try again.")
        else:
            st.warning("No journeys found for the selected countries. Please try again.")

