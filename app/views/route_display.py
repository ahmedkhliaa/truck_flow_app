import streamlit as st
from streamlit_folium import st_folium
import folium

import folium
from streamlit_folium import st_folium

def display_routes(route_data, selected_year):
    """
    Display a map with all routes, with polyline width dependent on traffic flow
    and hover tooltips showing traffic flow details.

    Args:
        route_data (DataFrame): A DataFrame containing route details, including coordinates and traffic flows.
                                Expected columns: "Start Coordinates", "End Coordinates", "Route Coordinates",
                                "Traffic Flow (2010)", "Traffic Flow (2019)", "Traffic Flow (2030)".
        selected_year (int): The year to visualize traffic flow (e.g., 2010, 2019, 2030).
    """
    if route_data.empty:
        st.write("No routes to display.")
        return

    # Initialize the map at the center of the first route's start coordinates
    first_route_start = route_data.iloc[0]["Start Coordinates"]
    route_map = folium.Map(location=first_route_start, zoom_start=7)

    # Add routes to the map
    for _, row in route_data.iterrows():
        # Extract route data
        route_coordinates = row["Route Coordinates"]
        traffic_flow = row[f"Traffic Flow ({selected_year})"]

        # Determine polyline width based on traffic flow
        polyline_width = max(1, traffic_flow // 50)  # Scale traffic flow to a reasonable width

        # Add polyline to the map
        folium.PolyLine(
            route_coordinates,
            color="blue",
            weight=polyline_width,
            tooltip=f"Traffic Flow ({selected_year}): {traffic_flow} trucks",
        ).add_to(route_map)

    # Display the map in Streamlit
    st_folium(route_map, width=1000, height=700)


