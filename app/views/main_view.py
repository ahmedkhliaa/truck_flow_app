import streamlit as st
from app.controllers.user_input_controller import handle_user_input
from app.controllers.prepare_routes_for_view import prepare_route_for_view
from app.controllers.journey_controller import *
from app.models.data_transformation import _cached_transformed_data
from app.views.route_display import *
import pandas as pd
from app.config import COUNTRIES

def render_app():
    """
    Main function to render the Streamlit app.
    """
    st.title("Transport Flow Visualization App")
    #st.write("Plan your routes by selecting origin and destination countries.")

    # Access cached transformed data
    edges_with_coordinates = _cached_transformed_data.get("edges_with_coordinates")
    truck_with_regions = _cached_transformed_data.get("truck_with_regions")

    if edges_with_coordinates.empty or truck_with_regions.empty:
        st.error("Data has not been preprocessed correctly. Please check your app setup.")
        return

    # User Input: Select origin and destination countries

    # Multi-selection dropdowns for origin and destination countries
    origin_countries = st.multiselect(
        label="Select Origin Countries",  # Label displayed above the dropdown
        options=COUNTRIES,  # List of options (unique origin countries)
        default=None,  # Default selection (None means no pre-selected values)
        key="origin_countries_dropdown",  # Unique key to identify the widget (optional but useful)
        help="Select one or more countries where the journeys originate",  # Tooltip text (optional)
    )
    destination_countries = st.multiselect(
        label="Select Destination Countries",
        options=COUNTRIES,
        default=None,
        help="Select one or more countries where the journeys are headed"
    )

    if origin_countries and destination_countries:
        # Handle user input to get country codes
        origin_codes, destination_codes = handle_user_input(origin_countries, destination_countries)

        # Filter journeys based on user selection
        filtered_journeys = filter_journeys_by_countries(origin_codes, destination_codes)
        st.write("Selected journeys based on your selection:", filtered_journeys) 

        if not filtered_journeys.empty:

            #Add radio buttons for year selection
            selected_year = st.radio(
                label="Select Year",
                options=[2010, 2019, 2030],
                index=0,  # Default to 2010
                help="Select the year to visualize traffic flow data."
            )

            #Show origin and destination region options
            origin_region_options = create_origin_region_options(filtered_journeys)
            destination_region_options = create_destination_region_options(filtered_journeys)

            # Let the user select origin and destination regions
            selected_origin_regions = st.multiselect(
                label="Select Origin Regions",
                options=sorted(origin_region_options)
            )

            selected_destination_regions = st.multiselect(
                label="Select Destination Regions",
                options=sorted(destination_region_options)
            )

            # Get the selected journey
            #selected_journey = select_jouney(selected_origin_region, selected_destination_region, filtered_journeys)    
            #st.write("Selected Journey:", selected_journey) 

            # Prepare the route for visualization
            # route_coordinates = prepare_route_for_view(selected_journey, edges_with_coordinates)
            
            # route_data =[{
            #         "Start Coordinates": route_coordinates[0],
            #         "End Coordinates": route_coordinates[-1],
            #         "Route Coordinates": route_coordinates,
            #         "Traffic Flow (2010)": selected_journey["Traffic_flow_trucks_2010"],
            #         "Traffic Flow (2019)": selected_journey["Traffic_flow_trucks_2019"],
            #         "Traffic Flow (2030)": selected_journey["Traffic_flow_trucks_2030"],
            #     }]
            
            # route_data = pd.DataFrame(route_data)
            # # Display the route on a map
            # display_route(route_data, selected_year)

            # Get the selected journeys
            selected_journeys = select_journeys(selected_origin_regions, selected_destination_regions, filtered_journeys)

            all_routes = []
            for _, journey in selected_journeys.iterrows():

                # Prepare the route for visualization
                route_coordinates = prepare_route_for_view(pd.DataFrame([journey]), edges_with_coordinates)
                all_routes.append({
                    "Start Coordinates": route_coordinates[0],
                    "End Coordinates": route_coordinates[-1],
                    "Route Coordinates": route_coordinates,
                    "Traffic Flow (2010)": journey["Traffic_flow_trucks_2010"],
                    "Traffic Flow (2019)": journey["Traffic_flow_trucks_2019"],
                    "Traffic Flow (2030)": journey["Traffic_flow_trucks_2030"],
                })
            
            # Convert to a Dataframe
            route_data = pd.DataFrame(all_routes)

            # Display the routes on a map
            display_routes(route_data, selected_year)
        else:
            st.warning("No journeys found for the selected countries. Please try again.")
