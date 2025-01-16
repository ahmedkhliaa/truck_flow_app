import streamlit as st

def render_year_selector():
    """
    Render the year selection UI.

    Returns:
        int: The selected year.
    """
    return st.radio(
        label="Select Year",
        options=[2010, 2019, 2030],
        index=0,
        help="Select the year to visualize traffic flow data.",
    )
