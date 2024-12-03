from app.controllers.filter_edges_by_path import filter_edges_by_path

def prepare_route_for_view(selected_journey, edges_with_coordinates):
    """
    Prepare the route data for visualization, combining origin, destination,
    and intermediate nodes into a single route structure.

    Args:
        filtered_journey (DataFrame): A single row DataFrame from the filtered journeys DataFrame.
        edges_with_coordinates (DataFrame): Preprocessed edges with coordinates.

    Returns:
        list: A list of coordinate pairs [(lat, lon), ...] representing the full route.
    """
    if selected_journey.empty:
        raise ValueError("No journey data found. Please check the input and try again.")    

    # Extract the first row from the DataFrame (assuming a single-row DataFrame)
    journey_row = selected_journey.iloc[0]

    # Extract necessary columns from the journey row
    origin_coordinates = (
        journey_row["Geometric_center_Y_origin"],  # Latitude
        journey_row["Geometric_center_X_origin"],  # Longitude
    )
    destination_coordinates = (
        journey_row["Geometric_center_Y_destination"],  # Latitude
        journey_row["Geometric_center_X_destination"],  # Longitude
    )

    # Extract Edge_path_E_road and convert to a list of node IDs
    edge_path = eval(journey_row["Edge_path_E_road"])  # Convert string to list if needed

    # Filter edges for the path
    filtered_edges = filter_edges_by_path(edge_path, edges_with_coordinates)

    # Construct the full route:
    # Start with the origin
    route_coordinates = [origin_coordinates]

    # Add intermediate nodes (edges)
    for _, row in filtered_edges.iterrows():
        start_node = (row["Network_Node_A_Y"], row["Network_Node_A_X"])  # Latitude, Longitude
        end_node = (row["Network_Node_B_Y"], row["Network_Node_B_X"])    # Latitude, Longitude
        # Add both nodes to the route if not already included
        if start_node not in route_coordinates:
            route_coordinates.append(start_node)
        if end_node not in route_coordinates:
            route_coordinates.append(end_node)

    # End with the destination
    route_coordinates.append(destination_coordinates)

    return route_coordinates
