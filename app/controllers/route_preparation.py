import pandas as pd
from app.controllers.prepare_routes_for_view import prepare_route_for_view

def prepare_routes(selected_journeys, edges_with_coordinates):
    """
    Prepare route data for visualization.

    Args:
        selected_journeys (DataFrame): The selected journeys DataFrame.
        edges_with_coordinates (DataFrame): Preprocessed edges with coordinates.

    Returns:
        DataFrame: Prepared route data with start/end coordinates, route path, and traffic flow data.
    """
    all_routes = []

    for _, journey in selected_journeys.iterrows():
        route_coordinates = prepare_route_for_view(journey, edges_with_coordinates)
        all_routes.append({
            "Start Coordinates": route_coordinates[0],
            "End Coordinates": route_coordinates[-1],
            "Route Coordinates": route_coordinates,
            "Traffic Flow (2010)": journey["Traffic_flow_trucks_2010"],
            "Traffic Flow (2019)": journey["Traffic_flow_trucks_2019"],
            "Traffic Flow (2030)": journey["Traffic_flow_trucks_2030"],
        })

    return pd.DataFrame(all_routes)
