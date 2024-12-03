from folium import Map
from streamlit_folium import st_folium

def display_empty_map():
    """
    Display an empty map centered on a default location.
    """
    empty_map = Map(location=[48.8566, 2.3522], zoom_start=4)  # Centered in Europe
    st_folium(empty_map, width=700, height=500)
