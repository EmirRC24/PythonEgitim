import folium
import pandas
import xlrd

harita = folium.Map(tiles="Cartodb positron")

veri = pandas.read_excel("tr-cities.xlsx")

enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
isimler = list(veri["City"])

for enlem, boylam, isim in zip(enlemler, boylamlar, isimler):
    harita.add_child(folium.Marker(location=(enlem, boylam),
                                   icon=folium.Icon(color="green"), popup=isim))


harita.save("Proje Deneme.html")
