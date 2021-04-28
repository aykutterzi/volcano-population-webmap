import folium
import pandas

data = pandas.read_csv("./Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_generator(elevation):
    if elevation < 100:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38, -99], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    data_frame = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=6,
            popup=folium.Popup(data_frame),
            icon=folium.Icon(color=color_generator(el)),
            fill_color=color_generator(el),
            color="grey",
            fill_opacity=0.7,
        )
    )

fg.add_child(folium.GeoJson(data=(open("world.json", "r", encoding="utf-8-sig").read())))


map.add_child(fg)

map.save("Map1.html")
