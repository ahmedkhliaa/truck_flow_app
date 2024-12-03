import pandas as pd
from app.config import FILE_PATHS, COUNTRY_MAPPING_PATH
import json

# Cached data storage
_cached_data = {}

def load_truck_traffic(chunk_size=500_000):
    """
    Load the Trucktrafficflow CSV file in chunks and cache it in memory.
    Args:
        chunk_size (int): Number of rows to read per chunk.
    Returns:
        DataFrame: Entire truck traffic data loaded into memory.
    """
    global _cached_data
    if "truck_traffic" not in _cached_data:
        print(f"Loading file: {FILE_PATHS['truck_traffic']}")  # Debug print
        print("Loading truck traffic data in chunks...")
        chunks = []
        for chunk in pd.read_csv(FILE_PATHS["truck_traffic"], chunksize=chunk_size):
            chunks.append(chunk)
        _cached_data["truck_traffic"] = pd.concat(chunks, ignore_index=True)
        print("Truck traffic data loaded into memory.")
    return _cached_data["truck_traffic"]

def load_nuts_regions():
    """
    Load the NUTS-3 regions CSV file into memory and cache it.
    Returns:
        DataFrame: NUTS-3 regions data.
    """
    global _cached_data
    if "nuts_regions" not in _cached_data:
        print("Loading NUTS-3 regions data...")
        _cached_data["nuts_regions"] = pd.read_csv(FILE_PATHS["nuts_regions"])
    return _cached_data["nuts_regions"]

def load_network_nodes():
    """
    Load the network nodes CSV file into memory and cache it.
    Returns:
        DataFrame: Nodes data.
    """
    global _cached_data
    if "network_nodes" not in _cached_data:
        print("Loading network nodes data...")
        _cached_data["network_nodes"] = pd.read_csv(FILE_PATHS["network_nodes"])
    return _cached_data["network_nodes"]

def load_network_edges():
    """
    Load the network edges CSV file into memory and cache it.
    Returns:
        DataFrame: Edges data.
    """
    global _cached_data
    if "network_edges" not in _cached_data:
        print("Loading network edges data...")
        _cached_data["network_edges"] = pd.read_csv(FILE_PATHS["network_edges"])
    return _cached_data["network_edges"]

def load_country_mapping():
    """
    Load the country mapping JSON file into memory and cache it.
    Returns:
        dict: Country code to name mapping.
    """
    global _cached_data
    if "country_mapping" not in _cached_data:
        print("Loading country mapping data...")
        with open(COUNTRY_MAPPING_PATH, "r") as file:
            _cached_data["country_mapping"] = json.load(file)
    return _cached_data["country_mapping"]


def load_all_data():
    """
    Load and cache all datasets into memory.
    Returns:
        dict: A dictionary containing all datasets as Pandas DataFrames.
    """
    global _cached_data
    if not _cached_data:  # Load all data only if not already cached
        print("Loading all datasets into memory...")
        load_truck_traffic()   # Load truck traffic data
        load_nuts_regions()    # Load NUTS-3 regions data
        load_network_nodes()   # Load network nodes data
        load_network_edges()   # Load network edges data
        load_country_mapping()     # Load country mapping data
        print("All datasets loaded into memory.")
    return _cached_data

def get_data(table_name):
    """
    Retrieve a specific dataset from the cached data.
    Args:
        table_name (str): The name of the table (e.g., "truck_traffic").
    Returns:
        DataFrame: The requested dataset as a Pandas DataFrame.
    """
    global _cached_data
    if not _cached_data:
        load_all_data()  # Ensure all data is loaded
    return _cached_data.get(table_name)

