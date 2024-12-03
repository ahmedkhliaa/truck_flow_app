from app.models.data_loader import get_data

_cached_transformed_data = {}

def preprocess_truck_traffic_with_regions():
    """
    Preprocess Truck Traffic Flow by joining it with NUTS-3 Regions.
    Returns:
        DataFrame: Preprocessed traffic flow data.
    """
    global _cached_transformed_data

    if "truck_with_regions" not in _cached_transformed_data:
        print("Preprocessing truck traffic with regions...")

        # Access cached raw data
        truck_traffic = get_data("truck_traffic")
        nuts_regions = get_data("nuts_regions")

        # Perform the joins
        truck_with_regions = truck_traffic.merge(
            nuts_regions,
            how="left",
            left_on="ID_origin_region",
            right_on="ETISPlus_Zone_ID",
            suffixes=("_origin", "_destination")
        ).merge(
            nuts_regions,
            how="left",
            left_on="ID_destination_region",
            right_on="ETISPlus_Zone_ID",
            suffixes=("_origin", "_destination")
        )

        # Drop redundant columns
        truck_with_regions = truck_with_regions.drop(columns=["ETISPlus_Zone_ID_origin", "ETISPlus_Zone_ID_destination"])
        
        # Cache the preprocessed data
        _cached_transformed_data["truck_with_regions"] = truck_with_regions
        print("Preprocessing completed.")

    return _cached_transformed_data["truck_with_regions"]

def preprocess_edges_with_coordinates():
    """
    Preprocess Network Edges by joining with Network Nodes to add coordinates.
    Returns:
        DataFrame: Preprocessed edges with node coordinates.
    """
    global _cached_transformed_data

    if "edges_with_coordinates" not in _cached_transformed_data:
        print("Preprocessing network edges with coordinates...")

        # Access cached raw data
        network_edges = get_data("network_edges")
        network_nodes = get_data("network_nodes")

        # Join edges with nodes to get coordinates of start and end points
        edges_with_coordinates = network_edges.merge(
            network_nodes,
            how="left",
            left_on="Network_Node_A_ID",
            right_on="Network_Node_ID"
        ).rename(
            columns={"Network_Node_X": "Network_Node_A_X", "Network_Node_Y": "Network_Node_A_Y"}
        ).merge(
            network_nodes,
            how="left",
            left_on="Network_Node_B_ID",
            right_on="Network_Node_ID"
        ).rename(
            columns={"Network_Node_X": "Network_Node_B_X", "Network_Node_Y": "Network_Node_B_Y"}
        )

        # Drop redundant columns
        edges_with_coordinates = edges_with_coordinates.drop(columns=["Network_Node_ID_x", "Network_Node_ID_y"])

        # Cache the preprocessed data
        _cached_transformed_data["edges_with_coordinates"] = edges_with_coordinates
        print("Network edges preprocessing completed.")
        # save only the head of the edges_with_coordinates to a CSV file
        edges_with_coordinates.head().to_csv("edges_with_coordinates.csv", index=False)

    return _cached_transformed_data["edges_with_coordinates"]

