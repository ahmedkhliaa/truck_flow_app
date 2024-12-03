import os

# Root directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Data directory
DATA_DIR = os.path.join(BASE_DIR, "data")

# Path to country mapping JSON
COUNTRY_MAPPING_PATH = os.path.join(DATA_DIR, "country_mapping.json")

# Paths for CSV files
FILE_PATHS = {
    "truck_traffic": os.path.join(DATA_DIR, "01_Trucktrafficflow.csv"),
    "nuts_regions": os.path.join(DATA_DIR, "02_NUTS-3-Regions.csv"),
    "network_nodes": os.path.join(DATA_DIR, "03_network-nodes.csv"),
    "network_edges": os.path.join(DATA_DIR, "04_network-edges.csv"),
}

# List of the countries to show in the dropdown
COUNTRIES = sorted([
    "France", "Portugal", "Spain", "Morocco", "Ireland", "Norway",
    "United Kingdom", "Gibraltar", "Andorra", "Belgium", "Netherlands",
    "Germany", "Switzerland", "Luxembourg", "Italy", "Denmark",
    "Liechtenstein", "Austria", "San Marino", "Czech Republic", "Sweden",
    "Slovenia", "Croatia", "Poland", "Bosnia and Herzegovina", "Hungary",
    "Montenegro", "Serbia", "Greece", "Finland", "North Macedonia", "Russia",
    "Romania", "Lithuania", "Latvia", "Bulgaria", "Ukraine", "Estonia",
    "Belarus", "Turkey", "Cyprus", "Kazakhstan", "Slovakia"
])

