import pandas as pd
from app.models.data_transformation import preprocess_truck_traffic_with_regions
from app.models.data_loader import _cached_data  # Use the cache for test mocking
from app.models.data_transformation import preprocess_edges_with_coordinates

def test_preprocess_truck_traffic_with_regions():
    # Mock the raw data in the cache
    _cached_data["truck_traffic"] = pd.DataFrame({
        "ID_origin_region": [101, 103],
        "ID_dest_region": [202, 202],
        "Edge_path_E_road": [["E1", "E2"], ["E3", "E4"]],
        "Total_distance": [1050, 1200]
    })
    _cached_data["nuts_regions"] = pd.DataFrame({
        "ETISPlus_Zone_ID": [101, 103, 202],
        "Name": ["Paris", "Lyon", "Berlin"],
        "Country": ["FR", "FR", "DE"]
    })

    # Call the transformation function
    preprocessed_data = preprocess_truck_traffic_with_regions()

    # Define expected output
    expected_data = pd.DataFrame({
        "ID_origin_region": [101, 103],
        "ID_dest_region": [202, 202],
        "Edge_path_E_road": [["E1", "E2"], ["E3", "E4"]],
        "Total_distance": [1050, 1200],
        "Name_origin": ["Paris", "Lyon"],
        "Country_origin": ["FR", "FR"],
        "Name_destination": ["Berlin", "Berlin"],
        "Country_destination": ["DE", "DE"]
    })

    # Assert the results match the expected DataFrame
    pd.testing.assert_frame_equal(preprocessed_data, expected_data, check_like=True)

def test_preprocess_edges_with_coordinates():
    # Mock the raw data in the cache
    _cached_data["network_edges"] = pd.DataFrame({
        "Network_Edge_ID": ["E1", "E2"],
        "Network_Node_A_ID": ["A1", "B1"],
        "Network_Node_B_ID": ["B1", "C1"],
        "Distance": [150, 200],
        "Traffic_flow_trucks_2019": [1000, 800],
        "Traffic_flow_trucks_2030": [1200, 1000]
    })
    _cached_data["network_nodes"] = pd.DataFrame({
        "Network_Node_ID": ["A1", "B1", "C1"],
        "Network_Node_X": [12.34, 23.45, 34.56],
        "Network_Node_Y": [56.78, 67.89, 78.90]
    })

    # Call the transformation function
    preprocessed_data = preprocess_edges_with_coordinates()

    # Define expected output
    expected_data = pd.DataFrame({
        "Network_Edge_ID": ["E1", "E2"],
        "Network_Node_A_ID": ["A1", "B1"],
        "Network_Node_B_ID": ["B1", "C1"],
        "Distance": [150, 200],
        "Traffic_flow_trucks_2019": [1000, 800],
        "Traffic_flow_trucks_2030": [1200, 1000],
        "Network_Node_A_X": [12.34, 23.45],
        "Network_Node_A_Y": [56.78, 67.89],
        "Network_Node_B_X": [23.45, 34.56],
        "Network_Node_B_Y": [67.89, 78.90]
    })

    # Assert the results match the expected DataFrame
    pd.testing.assert_frame_equal(preprocessed_data, expected_data, check_like=True)