from app.controllers.filter_edges_by_path import filter_edges_by_path
import streamlit as st

def prepare_route_for_view(selected_journey, edges_with_coordinates):
    """
    Prepare the route data for visualization, combining origin, destination,
    and intermediate nodes into a single route structure.

    Args:
        selected_journey (DataFrame): A single row DataFrame from the filtered journeys DataFrame.
        edges_with_coordinates (DataFrame): Preprocessed edges with coordinates.

    Returns:
        list: A list of coordinate pairs [(lat, lon), ...] representing the full route.
    """
    if selected_journey.empty:
        raise ValueError("No journey data found. Please check the input and try again.")    

    # Extract necessary columns from the journey row
    origin_coordinates = (
        selected_journey["geometric_centre_y_origin_region"],  # Latitude
        selected_journey["geometric_centre_x_origin_region"],  # Longitude
    )
    destination_coordinates = (
        selected_journey["geometric_centre_y_destination_region"],  # Latitude
        selected_journey["geometric_centre_x_destination_region"],  # Longitude
    )

    # Extract Edge_path_E_road and convert to a list of node IDs
    edge_path = eval(selected_journey["edge_path_e_road"])  # Convert string to list if needed

    # Filter edges for the path
    filtered_edges = filter_edges_by_path(edge_path, edges_with_coordinates)
    #st.write("retrieved edges", filtered_edges)

    # Construct the full route:
    # Start with the origin
    route_coordinates = [origin_coordinates]

    # Add intermediate nodes (edges)
    list_coordinates=[]
    for _, row in filtered_edges.iterrows():
        start_node = (row["network_node_a_y"], row["network_node_a_x"])  # Latitude, Longitude
        end_node = (row["network_node_b_y"], row["network_node_b_x"])    # Latitude, Longitude
        # Add both nodes to the route if not already included
        # if start_node not in route_coordinates:
        #     route_coordinates.append(start_node)
        # if end_node not in route_coordinates:
        #     route_coordinates.append(end_node)
        list_coordinates.append([start_node, end_node])
    route_coordinates.append(list_coordinates)
    # End with the destination
    route_coordinates.append(destination_coordinates)

    return route_coordinates
