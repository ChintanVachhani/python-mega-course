import folium as fol
import pandas as pd

volcanoesData = pd.read_csv("Volcanoes_USA.txt")
latitudesList = list(volcanoesData["LAT"])
longitudesList = list(volcanoesData["LON"])
elevationsList = list(volcanoesData["ELEV"])


def marker_color_picker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


webMap = fol.Map(location=[37.3410412, -121.8943972], zoom_start=4, tiles="Mapbox Bright")
volcanoesFeatureGroup = fol.FeatureGroup(name="Volcanoes")
for lt, ln, el in zip(latitudesList, longitudesList, elevationsList):
    volcanoesFeatureGroup.add_child(fol.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m",
                                                     fill_color=marker_color_picker(el), fill=True, color='grey',
                                                     fill_opacity=0.7))

populationFeatureGroup = fol.FeatureGroup(name="Population")

populationFeatureGroup.add_child(fol.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                             style_function=lambda x: {
                                                 'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                 else 'orange' if 10000000 <= x['properties'][
                                                     'POP2005'] < 20000000 else 'red'}))

webMap.add_child(populationFeatureGroup)
webMap.add_child(volcanoesFeatureGroup)
webMap.add_child(fol.LayerControl())
webMap.save("web-map.html")
