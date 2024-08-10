import folium
import pandas

veri = pandas.read_excel("world_coronavirus_cases.xlsx")

enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
toplamVaka = list(veri["Toplam Vaka"])

world_map = folium.Map(tiles="Cartodb positron")


for enlem, boylam in zip(enlemler, boylamlar):
    world_map.add_child(folium.Circle(location=(enlem,boylam), radius=100000, color="blue", fill_color="green", fill_opacity=1))

world_map.save("World_map.html")