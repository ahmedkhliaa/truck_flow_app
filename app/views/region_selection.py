import streamlit as st
from app.controllers.journey_controller import create_origin_region_options, create_destination_region_options

def render_region_selection(filtered_journeys):
    """
    Render the UI for selecting origin and destination regions.

    Args:
        filtered_journeys (DataFrame): The filtered journeys DataFrame.

    Returns:
        tuple: Lists of selected origin and destination regions.
    """
    origin_regions = create_origin_region_options(filtered_journeys)
    destination_regions = create_destination_region_options(filtered_journeys)

    selected_origin_regions = st.multiselect(
        label="Select Origin Regions",
        options=sorted(origin_regions),
        help="Select one or more regions for the origin.",
    )

    selected_destination_regions = st.multiselect(
        label="Select Destination Regions",
        options=sorted(destination_regions),
        help="Select one or more regions for the destination.",
    )

    return selected_origin_regions, selected_destination_regions
