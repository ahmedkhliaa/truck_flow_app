from app.models.data_transformation import _cached_transformed_data

def filter_journeys_by_countries(origin_codes, destination_codes):
    """
    Filter journeys based on origin and destination country codes.
    Args:
        origin_codes (list): List of origin country codes (e.g., ['FR', 'DE']).
        destination_codes (list): List of destination country codes (e.g., ['ES', 'IT']).
    Returns:
        DataFrame: Filtered journeys from truck_with_regions.
    """
    # Access the cached preprocessed data
    truck_with_regions = _cached_transformed_data.get("truck_with_regions")
    
    if truck_with_regions is None:
        raise ValueError("truck_with_regions has not been preprocessed and cached.")

    # Filter journeys matching the origin and destination codes
    filtered_journeys = truck_with_regions[
        (truck_with_regions["Country_origin"].isin(origin_codes)) &
        (truck_with_regions["Country_destination"].isin(destination_codes))
    ]

    return filtered_journeys

def create_origin_region_options(filtered_journeys):
    """
    Create a list of user-friendly origin region options.

    Args:
        filtered_journeys (DataFrame): Filtered journeys DataFrame.

    Returns:
        list: Origin region options as strings for display.
    """
    return filtered_journeys["Name_origin_region"].unique().tolist()

def create_destination_region_options(filtered_journeys):
    """
    Create a list of user-friendly destination region options.

    Args:
        filtered_journeys (DataFrame): Filtered journeys DataFrame.

    Returns:
        list: Destination region options as strings for display.
    """
    return filtered_journeys["Name_destination_region"].unique().tolist()


def select_jouney(origin_region, destination_region, filtered_journeys):
    """
    Select a journey based on the origin and destination regions.

    Args:
        origin_region (str): Selected origin region.
        destination_region (str): Selected destination region.
        filtered_journeys (DataFrame): Filtered journeys DataFrame.

    Returns:
        DataFrame: Selected journey based on the regions.
    """
    selected_journey = filtered_journeys[
        (filtered_journeys["Name_origin_region"] == origin_region) &
        (filtered_journeys["Name_destination_region"] == destination_region)
    ]
    return selected_journey

def select_journeys(origin_regions, destination_regions, filtered_journeys):
    """
    Select journeys based on the origin and destination regions.

    Args:
        origin_regions (list): Selected origin regions.
        destination_regions (list): Selected destination regions.
        filtered_journeys (DataFrame): Filtered journeys DataFrame.

    Returns:
        DataFrame: Selected journeys based on the regions.
    """
    selected_journeys = filtered_journeys[
        (filtered_journeys["Name_origin_region"].isin(origin_regions)) &
        (filtered_journeys["Name_destination_region"].isin(destination_regions))
    ]
    return selected_journeys

def create_journey_options(filtered_journeys):
    """
    Create a list of user-friendly journey options.

    Args:
        filtered_journeys (DataFrame): Filtered journeys DataFrame.

    Returns:
        list: Journey options as strings for display.
    """
    journey_options = []
    for _, row in filtered_journeys.iterrows():
        origin = row["Name_origin_region"]
        destination = row["Name_destination_region"]
        distance = row["Total_distance"]
        journey_options.append(f"{origin} → {destination} (Distance: {distance} km)")
    return journey_options


