import folium
import pandas

veri = pandas.read_excel("world_coronavirus_cases.xlsx")

enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
toplamVaka = list(veri["Toplam Vaka"])

def vaka_sayisi_renk(vaka):
    if vaka < 100000:
        return "green"
    elif vaka < 300000:
        return "white"
    elif vaka < 750000:
        return "orange"
    else:
        return "red"

def vaka_sayisi_radius(vaka):
    if vaka < 100000:
        return 40000
    elif vaka < 300000:
        return 100000
    elif vaka < 750000:
        return 200000
    else:
        return 400000


world_map = folium.Map(tiles="Cartodb positron")


for enlem, boylam, vaka in zip(enlemler, boylamlar, toplamVaka):
    world_map.add_child(folium.Circle(location=(enlem,boylam), radius=vaka_sayisi_radius(vaka), color=vaka_sayisi_renk(vaka), fill_color=vaka_sayisi_renk(vaka), fill_opacity=0.3))

world_map.save("World_map.html")