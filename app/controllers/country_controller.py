from app.models.data_loader import get_data  # Import the function to access cached data

def translate_country_name_to_code(country_name, mapping=None):
    """
    Translate a user-friendly country name to its country code.
    Args:
        country_name (str): The country name (e.g., 'France').
        mapping (dict): Optional; The country code mapping. If None, retrieves from cache.
    Returns:
        str: The corresponding country code (e.g., 'FR'), or None if not found.
    """
    if mapping is None:  # Load from cache if not provided
        mapping = get_data("country_mapping")
    reverse_mapping = {v: k for k, v in mapping.items()}  # Reverse the mapping
    return reverse_mapping.get(country_name)

def translate_multiple_countries(country_names, mapping=None):
    """
    Translate a list of user-friendly country names to their corresponding codes.
    Args:
        country_names (list): List of country names (e.g., ['France', 'Germany']).
        mapping (dict): Optional; The country code mapping. If None, retrieves from cache.
    Returns:
        list: List of corresponding country codes (e.g., ['FR', 'DE']).
    """
    if mapping is None:  # Load from cache if not provided
        mapping = get_data("country_mapping")
    reverse_mapping = {v: k for k, v in mapping.items()}  # Reverse the mapping
    return [reverse_mapping.get(name) for name in country_names if reverse_mapping.get(name) is not None]
