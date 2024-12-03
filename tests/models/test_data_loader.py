import pytest
import pandas as pd
from app.models.data_loader import (
    load_truck_traffic,
    load_nuts_regions,
    load_network_nodes,
    load_network_edges,
    load_country_mapping,
    load_all_data,
    _cached_data
)
from app.config import FILE_PATHS


def test_load_truck_traffic():
    data = load_truck_traffic()
    assert not data.empty, "Truck traffic data should not be empty"


def test_load_nuts_regions():
    data = load_nuts_regions()
    assert not data.empty, "NUTS-3 regions data should not be empty"


def test_load_network_nodes():
    data = load_network_nodes()
    assert not data.empty, "Network nodes data should not be empty"


def test_load_network_edges():
    data = load_network_edges()
    assert not data.empty, "Network edges data should not be empty"


def test_load_country_mapping():
    data = load_country_mapping()
    assert isinstance(data, dict), "Country mapping should be a dictionary"
    assert len(data) > 0, "Country mapping data should not be empty"


def test_data_is_cached():
    global _cached_data
    _cached_data.clear()  # Clear cache before testing
    load_all_data()  # Load all data
    assert "truck_traffic" in _cached_data, "Truck traffic data should be cached"
    assert "nuts_regions" in _cached_data, "NUTS-3 regions data should be cached"
    assert "network_nodes" in _cached_data, "Network nodes data should be cached"
    assert "network_edges" in _cached_data, "Network edges data should be cached"
    assert "country_mapping" in _cached_data, "Country mapping data should be cached"


# def test_invalid_file_path(monkeypatch):
#     # Temporarily modify FILE_PATHS to use an invalid path
#     invalid_paths = FILE_PATHS.copy()
#     invalid_paths["truck_traffic"] = "invalid_path.csv"
    
#     monkeypatch.setattr("app.models.data_loader.FILE_PATHS", invalid_paths)
#     print(FILE_PATHS)  # This should show the modified "invalid_path.csv" path

#     with pytest.raises(FileNotFoundError):
#         load_truck_traffic()


def test_load_all_data():
    data = load_all_data()
    assert "truck_traffic" in data, "Truck traffic should be in cached data"
    assert "nuts_regions" in data, "NUTS-3 regions should be in cached data"
    assert "network_nodes" in data, "Network nodes should be in cached data"
    assert "network_edges" in data, "Network edges should be in cached data"
    assert "country_mapping" in data, "Country mapping should be in cached data"


def test_load_truck_traffic_mock(monkeypatch):
    def mock_read_csv(*args, **kwargs):
        return pd.DataFrame({"ID_origin_region": [1], "ID_dest_region": [2]})
    
    monkeypatch.setattr("pandas.read_csv", mock_read_csv)
    data = load_truck_traffic()
    assert not data.empty, "Mocked truck traffic data should not be empty"


