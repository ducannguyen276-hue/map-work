import folium
from folium.plugins import Draw
from streamlit_folium import st_folium
import streamlit as st

m = folium.Map(location=[43.4720, -80.5400], zoom_start=12)

# Add Draw plugin configured ONLY for markers
Draw(
    export=False,
    draw_options={
        "polyline": False,
        "polygon": False,
        "circle": False,
        "rectangle": False,
        "circlemarker": False,
        "marker": True,
    },
).add_to(m)

map_data = st_folium(m, height=500, width=700)

# Print all placed markers
if map_data and map_data.get("all_drawings"):
    for i, drawing in enumerate(map_data["all_drawings"]):
        # Note: GeoJSON stores coordinates as [longitude, latitude]
        lng, lat = drawing["geometry"]["coordinates"]
        print(f"Marker {i+1}: Lat={lat}, Lng={lng}")
        st.write(f"Marker {i+1}: Lat={lat}, Lng={lng}")