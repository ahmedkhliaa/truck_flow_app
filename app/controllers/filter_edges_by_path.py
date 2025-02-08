from app.models.data_transformation import preprocess_edges_with_coordinates

def filter_edges_by_path(edge_path, edges_with_coordinates):
    """
    Filter the `edges_with_coordinates` DataFrame to include only the edges
    corresponding to the `Edge_path_E_road` (list of node IDs) for a specific journey.

    Args:
        edge_path (list): List of node IDs defining the route (e.g., [1000218, 1035423]).
        edges_with_coordinates (DataFrame): Preprocessed edges with node coordinates.

    Returns:
        DataFrame: Filtered edges with their coordinates for the specified route.
    """
    if edges_with_coordinates is None:
        # Ensure edges_with_coordinates is preprocessed
        edges_with_coordinates = preprocess_edges_with_coordinates()

    # Filter edges where both nodes (A and B) exist in the edge path
    filtered_edges = edges_with_coordinates[
        (edges_with_coordinates["Network_Edge_ID"].isin(edge_path))]

    # Ensure the edges are in the correct order along the path
    #filtered_edges = filtered_edges.sort_values(by=["Network_Node_A_ID", "Network_Node_B_ID"])

    return filtered_edges
