import folium

harita = folium.Map(location=[41, 29],tiles="Stamen Toner",attr='Emir')

harita.save("Deneme.html")
