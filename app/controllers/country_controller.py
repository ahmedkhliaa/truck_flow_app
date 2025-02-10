from app.models.data_loader import load_country_mapping

def translate_multiple_countries(country_names, mapping=None):
    """
    Translate a list of user-friendly country names to their corresponding codes.
    Args:
        country_names (list): List of country names (e.g., ['France', 'Germany']).
        mapping (dict): Optional; The country code mapping. If None, retrieves from cache.
    Returns:
        list: List of corresponding country codes (e.g., ['FR', 'DE']).
    """
    mapping = load_country_mapping()

    reverse_mapping = {v: k for k, v in mapping.items()}  # Reverse the mapping
    return [reverse_mapping.get(name) for name in country_names if reverse_mapping.get(name) is not None]
