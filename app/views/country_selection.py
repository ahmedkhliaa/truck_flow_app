import streamlit as st
from app.config import COUNTRIES

def render_country_selection():
    """
    Render the UI for selecting origin and destination countries.

    Returns:
        tuple: Lists of selected origin and destination countries.
    """
    origin_countries = st.multiselect(
        label="Select Origin Countries",
        options=COUNTRIES,
        default=None,
        help="Select one or more countries where the journeys originate.",
    )

    destination_countries = st.multiselect(
        label="Select Destination Countries",
        options=COUNTRIES,
        default=None,
        help="Select one or more countries where the journeys are headed.",
    )

    return origin_countries, destination_countries
