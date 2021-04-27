import folium

map = folium.Map(location=[37, 15], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[37, 15], [41, 14]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi, Etna here!", icon=folium.Icon(color="green")))


map.add_child((fg))

map.save("Map1.html")
