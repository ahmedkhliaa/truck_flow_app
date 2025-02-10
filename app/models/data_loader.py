from app.config import COUNTRY_MAPPING_PATH
import json
from app.models.db_connection import execute_query

def load_edge_with_node_coordinates_data():

    query = f"""
            SELECT 
                ne.network_edge_id,
                ne.network_node_a_id,
                ne.network_node_b_id,
                nn_a.network_node_x AS network_node_a_x,
                nn_a.network_node_y AS network_node_a_y,
                nn_b.network_node_x AS network_node_b_x,
                nn_b.network_node_y AS network_node_b_y
            FROM 
                network_edges AS ne
            LEFT JOIN network_nodes AS nn_a
                ON ne.network_node_a_id = nn_a.network_node_id
            LEFT JOIN network_nodes AS nn_b
                ON ne.network_node_b_id = nn_b.network_node_id;
    """

    return execute_query(query)

def load_country_mapping():
    """
    Load the country mapping JSON file .
    Returns:
        dict: Country code to name mapping.
    """
    with open(COUNTRY_MAPPING_PATH, "r") as file:
        return (json.load(file))


