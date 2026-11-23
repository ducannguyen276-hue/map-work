import folium

# Example study locations: name and [latitude, longitude]
study_locations = {
    "Library": [43.4720, -80.5440],
    "Campus": [43.4750, -80.5400],
    "Cafe": [43.4700, -80.5250],
}

# Create a map centred around Waterloo
m = folium.Map(location=[43.4720, -80.5400], zoom_start=14)

# Add a marker for each location
for name, coordinates in study_locations.items():
    folium.Marker(
        location=coordinates,
        popup=name,
        tooltip=name
    ).add_to(m)

# Add lines between the locations in dictionary order
folium.PolyLine(
    locations=list(study_locations.values()),
    color="blue",
    weight=4,
    tooltip="Study locations"
).add_to(m)

m.save("study_map.html")