import requests
from bs4 import BeautifulSoup
import pandas as pd
import folium
# Sayı olan değerleri ayıklayıp yazdırmak için
import re
import time
import webbrowser


class Indicators():
    def __init__(self):
        self.dongu=True

    def program(self):
        secim=self.menu()

        if secim == "1":
            print("Trade Balance Verisi Alınıyor...\n")
            time.sleep(2)
            self.trade_balance()
        
        if secim == "2":
            print("Nüfus Dağılım Verisi Alınıyor")
            time.sleep(2)
            self.nufus_dagilim()

        if secim == "3":
            print("Inflation Verileri Alınıyor...\n")
            time.sleep(2)
            self.inflation()

        if secim == "4":
            print("Ana Verileri Haritaya İşle")


        if secim == "4":
            print("Daha Fazla Veri Aktarılıyor\n")
            time.sleep(2)
            self.daha_fazla_veri()
        if secim == "5":
            print("Programdan çıkılıyor...\n")
            time.sleep(2)
            self.cikis()



    def menu(self):
        def kontrol(secim): # ana veriler icin
            if not re.search("[1-6]",secim):
                raise Exception("Lutfen 1 ve 6 Arasinda Gecerli Bir Secim Yapın!!")
            elif len(secim)!=1:
                raise Exception(("Lutfen 1 ve 6 Arasinda Gecerli Bir Secim Yapın!!"))
        while True:
            try:
                secim=input("\n\nMerhabalar, FuzionFolium Menusune Hos Geldiniz...\n\nLutfen Yapmak İstediginiz İslemi Seciniz...\
                         \n[1]Trade Balance İndikatörü\n[2]Nufüs Dağılım Oranı\n[3]Enflasyon\n[n]Daha Fazla Veriye Eriş\n[5]Cıkış\nSeçim:  ")
            except  Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        return secim                


    def daha_fazla_veri(self):
        pass
    def nufus_dagilim(self):
        nufus_dagilim_haritasi = folium.FeatureGroup(name="NüfusDağılımHaritası")
        world_map = folium.Map(tiles="Cartodb dark_matter")
        nufus_dagilim_haritasi.add_child(folium.GeoJson(
                            data=(open("C:/Users/batuh/OneDrive/Masaüstü/corona_harita/Python Core Veri Projesi/world.json"
                                       , "r", encoding="utf-8-sig").read()),
                            style_function= lambda x : {'fillColor':'green'
                            if x["properties"]["POP2005"] < 20000000 else 'white'
                            if 20000000 <= x["properties"]["POP2005"]  <= 50000000 else 'orange'
                            if 50000000 <= x["properties"]["POP2005"] <= 100000000 else 'red'}))
        world_map.add_child(nufus_dagilim_haritasi)
        world_map.add_child(folium.LayerControl())
        world_map.save("map1.html")
        print("Nüfus Dağılım Verisi Haritaya İşlendi")
    
    def trade_balance(self):
        tercih = input("Tercihinizi Giriniz...\n[1]Veriyi Haritada Görselleştir\n[2]Güncel Veriyi Ekrana Getir\n[3]Güncel Veriyi Excele Aktar\nTercih:")
        if tercih == "1":
            veri = pd.read_excel("C:/Users/batuh/OneDrive/Masaüstü/corona_harita/Python Core Veri Projesi/Ratings.xlsx")
            enlemler = list(veri["Enlem"])
            boylamlar = list(veri["Boylam"])
            CO2_Emission = list(veri["esas"])

            total_CO2_Emission_Map = folium.FeatureGroup(name="Trade Balance")

            def CO2_Emission_renk(emission):
                if emission is None:
                    return "black"
                elif emission > 300:
                    return "green"
                elif emission > 60:
                    return "white"
                elif emission > 5:
                    return "yellow"
                elif emission > -50:
                    return "orange"
                else:
                    return "red"

            def CO2_Emission_yari_cap(vaka):
                if vaka > 400:
                    return 50000
                elif vaka > 60:
                    return 60000
                elif vaka > 5:
                    return 70000
                elif vaka > -20:
                    return 100000
                elif vaka == None:
                    return 150000
                else:
                    return 200000
            world_map = folium.Map(tiles="Cartodb dark_matter")
            for enlem, boylam, emission in zip(enlemler,boylamlar,CO2_Emission): #
                total_CO2_Emission_Map.add_child(folium.Circle(location=(enlem, boylam),
                                                 radius=CO2_Emission_yari_cap(emission),
                                                 color=CO2_Emission_renk(emission),
                                                 fill=CO2_Emission_renk(emission),
                                                 fill_opacity=0.5))
            
            world_map.add_child(total_CO2_Emission_Map)
            world_map.add_child(folium.LayerControl())
            world_map.save("map1.html")
            time.sleep(2)
            print("Trade Balance Verisi Haritaya İşlendi... ")
            t_b = input("Harita Açılsın mı?[E/H]")
            if t_b == 'E':
                print("Harita Açılıyor")
                time.sleep(2)
                html_file_path = 'C:/Users/batuh/OneDrive/Masaüstü/corona_harita/map1.html'

    
                webbrowser.open(html_file_path)
            else:
                print("Harita açılmadı.")


        
        if tercih == "2":
            print("\nGüncel Veri Ekrana Yazdırılıyor...\n")
            time.sleep(2)
            url = "https://www.theglobaleconomy.com/rankings/trade_balance_dollars/"


            response = requests.get(url)
            response.raise_for_status()
        #    HTTP isteği başarılı mı kontrol eder

        # BeautifulSoup ile HTML içeriğini parse edin
            parser = BeautifulSoup(response.content, 'html.parser')

            ülkeler = ["Albania","Algeria","Angola","Antigua-and-Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan",
"Bahrain","Bangladesh","Belarus","Belgium","Belize","Bhutan","Bolivia","Bosnia-and-Herzegovina","Brazil","Bulgaria",
"Cambodia","Canada","Cape-Verde","Chile","China","Colombia","Costa-Rica","Croatia","Cyprus","Czech-Republic",
"Denmark","Dominican-Republic","Dominica",
"Ecuador","El-Salvador","Estonia","Ethiopia",
"Finland","France",
"Georgia","Germany","Greece","Grenada","Guatemala",
"Honduras","Hong-Kong","Hungary",
"Iceland","India","Indonesia","Ireland","Israel","Italy",
"Japan",
"Kazakhstan","Kuwait",
"Latvia","Lebanon","Lesotho","Lithuania","Luxembourg",
"Malaysia","Mauritius","Mexico","Moldova","Mongolia","Montenegro","Mozambique",
"Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Nigeria","Macedonia","Norway",
"Pakistan","Panama","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar",
"Romania","Russia","Rwanda",
"Saint-Lucia","Samoa","Saudi-Arabia","Serbia","Seychelles","Singapore","Slovakia","Slovenia","Solomon-Islands","South-Africa","South-Korea","Spain","Sri-Lanka","Saint-Vincent-and-the-Grenadines","Suriname","Sweden","Switzerland",
"Tajikistan","Thailand","Turkey",
"United-Kingdom","USA","Ukraine","Uruguay","Uzbekistan",
"Vietnam",
]

            frames = []
            for i in range(len(ülkeler)):
                table = parser.find("a", {"href":f"/{ülkeler[i]}/trade_balance_dollars/"}).parent.parent.find_all("td")
                bilgi1 = table[1].string
                bilgi2= table[0].a.string 
                item_str = str(bilgi1)
                        
                        # Temizleme işlemi: boşlukları ve özel karakterleri kaldırma
                cleaned_item = re.sub(r'[\r\n\t\s]+', '', item_str)
                frames.append({
                            'Country Name': bilgi2,
                            'Trade Balance': cleaned_item
                        })
            frame = pd.DataFrame(frames)
            print(frame)
        
            x = input("Güncel Veriler Excele Aktarılsın mı?[Evet/Hayır]\n")
            if x == "evet":
                farklı_excel = input("Veriler Farklı bir Excel dosyasına mı kaydedilsin[E/H]\n")
                if farklı_excel == "E":
                    dosya_konum = input("Verilerin işleneceği Excel dosyasının konumunu giriniz:")
                    try:
                        frame.to_excel(f"{dosya_konum}"\
                                           ,sheet_name="Trade_Balance",index=False)
                    except FileNotFoundError:
                        print("Dosya dizini hatalı girildi")
                                          
                elif farklı_excel == "H": # excel dosyaısnı baştan oluşturdu
                    with pd.ExcelWriter("C:/Users/batuh/OneDrive/Masaüstü/corona_harita/Python Core Veri Projesi/world_coronavirus_cases.xlsx")\
                        as writer:
                                frame.to_excel(writer,sheet_name="Trade_Balance",index=False) 
                else:
                    print("Hatalı komut!!")
            elif x == "hayır":
                print("Ana Menuye Donuluyor")
                time.sleep(2)
                self.menudon()
            else:
                    print("Hatalı komut!!")


#C:\Users\batuh\OneDrive\Masaüstü\corona_harita\Python Core Veri Projesi\world_coronavirus_cases.xlsx

    def inflation(self):
        pass

    def harita(self):#islem sonunda harita acılsın mı? Ana verilerin hepsini haritaya işler
        pass

    def toExcel(self):
        pass

    def veriyazdir(self):
        pass

    def cikis(self):
        self.dongu=False
        exit()


    def menudon(self):
        while True:
            x=input("Ana Menüye Dönmek için 7'ye Çıkmak için 5'e Basiniz")
            if x == "7":
                print("Ana Menuye Donuluyor")
                time.sleep(2)
                break
                self.program()
            elif x =="5":
                self.cikis
                break
            else:
                print("Lutfen Geçerli Bir Deger Giriniz.")





Sistem=Indicators()
while Sistem.dongu:
    Sistem.program()

#FileNotFoundError

"""url = "https://www.theglobaleconomy.com/rankings/trade_balance_dollars/"


response = requests.get(url)
response.raise_for_status()
# HTTP isteği başarılı mı kontrol eder

# BeautifulSoup ile HTML içeriğini parse edin
parser = BeautifulSoup(response.content, 'html.parser')

ülkeler = ["Albania","Algeria","Angola","Antigua-and-Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan",
"Bahrain","Bangladesh","Belarus","Belgium","Belize","Bhutan","Bolivia","Bosnia-and-Herzegovina","Brazil","Bulgaria",
"Cambodia","Canada","Cape-Verde","Chile","China","Colombia","Costa-Rica","Croatia","Cyprus","Czech-Republic",
"Denmark","Dominican-Republic","Dominica",
"Ecuador","El-Salvador","Estonia","Ethiopia",
"Finland","France",
"Georgia","Germany","Greece","Grenada","Guatemala",
"Honduras","Hong-Kong","Hungary",
"Iceland","India","Indonesia","Ireland","Israel","Italy",
"Japan",
"Kazakhstan","Kuwait",
"Latvia","Lebanon","Lesotho","Lithuania","Luxembourg",
"Malaysia","Mauritius","Mexico","Moldova","Mongolia","Montenegro","Mozambique",
"Namibia","Nepal","Netherlands","New-Zealand","Nicaragua","Nigeria","Macedonia","Norway",
"Pakistan","Panama","Paraguay","Peru","Philippines","Poland","Portugal",
"Qatar",
"Romania","Russia","Rwanda",
"Saint-Lucia","Samoa","Saudi-Arabia","Serbia","Seychelles","Singapore","Slovakia","Slovenia","Solomon-Islands","South-Africa","South-Korea","Spain","Sri-Lanka","Saint-Vincent-and-the-Grenadines","Suriname","Sweden","Switzerland",
"Tajikistan","Thailand","Turkey",
"United-Kingdom","USA","Ukraine","Uruguay","Uzbekistan",
"Vietnam",
]

frames = []
for i in range(len(ülkeler)):
    table = parser.find("a", {"href":f"/{ülkeler[i]}/trade_balance_dollars/"}).parent.parent.find_all("td")
    bilgi1 = table[1].string
    bilgi2= table[0].a.string 
    item_str = str(bilgi1)
                        
                        # Temizleme işlemi: boşlukları ve özel karakterleri kaldırma
    cleaned_item = re.sub(r'[\r\n\t\s]+', '', item_str)
    frames.append({
                            'Country Name': bilgi2,
                            'Trade Balance': cleaned_item
                        })
frame = pd.DataFrame(frames)
print(frame)
dosya = frame.to_excel("C:/Users/batuh/OneDrive/Masaüstü/corona_harita/Python Core Veri Projesi/bilgiler.xlsx",sheet_name="Trade_Balance",index=False) 
# tüm verileri tek sayfada toplayalım , sayfa adı veriler olsun su an trade_balance"""






ülkeler = ["Turkey", "Iceland", "Serbia", "Russia", "Czechia", "Slovakia", "Romania", "Poland", "San Marino", "Belarus", "Austria", "Hungary", "Croatia", "Ukraine", "Bulgaria", "Norway", "Andorra", "Montenegro", "Estonia", "Moldova", "France", "Malta", "Slovenia", "UK", "Albania", "Greece", "North Macedonia", "Spain", "Luxembourg", "Ireland", "Sweden", "Germany", "Bosnia & Herzegovina", "Cyprus", "Portugal", "Switzerland", "Finland", "Netherlands", "Latvia", "Lithuania", "Belgium", "Denmark", "Italy", "Haiti", "Jamaica", "Nicaragua", "Honduras", "Barbados", "Mexico", "Guatemala", "St. Vincent & the Grenadines", "Belize", "Dominican Republic", "Antigua & Barbuda", "USA", "Canada", "Grenada", "Dominica", "Aruba", "Saint Lucia", "Panama", "Bahamas", "Puerto Rico", "El Salvador", "Trinidad & Tobago", "Costa Rica"]