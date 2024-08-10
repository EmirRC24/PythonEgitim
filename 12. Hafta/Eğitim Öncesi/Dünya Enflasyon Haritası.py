import folium
import pandas as pd

veri = pd.read_excel("dunya_enflasyon_oranlari_guncel_v3.xlsx")

enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
enflasyon_oranlari = list(veri["Son"])

def enflasyon_renk(enflasyon):
    if enflasyon < 2:
        return "green"
    elif enflasyon < 5:
        return "orange"
    elif enflasyon < 10:
        return "red"
    else:
        return "darkred"

def enflasyon_radius(enflasyon):
    if enflasyon < 2:
        return 40000
    elif enflasyon < 5:
        return 100000
    elif enflasyon < 10:
        return 200000
    else:
        return 400000

world_map = folium.Map(tiles="Cartodb positron")

for enlem, boylam, enflasyon in zip(enlemler, boylamlar, enflasyon_oranlari):
    folium.Circle(
        location=(enlem, boylam),
        radius=enflasyon_radius(enflasyon),
        color=enflasyon_renk(enflasyon),
        fill_color=enflasyon_renk(enflasyon),
        fill_opacity=0.3
    ).add_to(world_map)

world_map.save("World_map.html")
