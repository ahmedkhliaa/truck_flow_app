from app.controllers.country_controller import translate_multiple_countries
from app.models.data_loader import load_country_mapping

def handle_user_input(origin_countries, destination_countries):
    """
    Handle user input to get the corresponding country codes.
    Args:
        origin_countries (list): List of origin countries as names (e.g., ['France', 'Germany']).
        destination_countries (list): List of destination countries as names (e.g., ['Spain', 'Italy']).
    Returns:
        tuple: Two lists of country codes for origin and destination countries.
    """
    # Load the country mapping
    mapping = load_country_mapping()

    # Translate the input countries to codes
    #origin_codes = translate_country_name_to_code(origin_countries, mapping)
    #destination_codes = translate_country_name_to_code(destination_countries, mapping)
    origin_codes = translate_multiple_countries(origin_countries, mapping)
    destination_codes = translate_multiple_countries(destination_countries, mapping)


    return origin_codes, destination_codes
