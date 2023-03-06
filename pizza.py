import csv
import datetime
import pandas as pd

class Pizza:

    def get_description(self):
        return self.description

    def get_cost(self): 
        return self.price
    
class Klasik(Pizza):
    name = "Klasik"
    price = 99.90
    description = "Klasik bir pizza."

class Margarita(Pizza):
    name = "Margarita"
    price = 79.90
    description = "Margarita bir pizza."

class TurkPizza(Pizza):
    name = "TurkPizza"
    price = 119.90
    description = "Türk bir pizza."

class SadePizza(Pizza):
    name = "SadePizza"
    price = 89.90
    description = "Sade bir pizza."

class Decorator(Pizza): 
   pass

class Zeytin(Decorator):
    name = "Zeytin"
    price = 2
    description = "Siyah Zeytin."
    
class Mantar(Decorator):
    name = "Mantar"
    price = 4
    description = "Beyaz Kültür Mantarı."

class KeciPeyniri(Decorator):
    name = "KeciPeyniri"
    price = 8
    description = "Beyaz Keçi Peyniri."

class Et(Decorator):
    name = "Et"
    price = 12
    description = "Kırmızı Et."

class Sogan(Decorator):
    name = "Sogan"
    price = 2
    description = "Beyaz Soğan."

class Misir(Decorator):
    name = "Misir"
    price = 2
    description = "Süt Mısır."

def pizzaSectir():
    secilenPizza = None
    while secilenPizza is None:
        pizzaSecimi = input("Bir pizza seciniz: ")
        if pizzaSecimi == '1':
            secilenPizza = Klasik()
        elif pizzaSecimi == '2':
            secilenPizza = Margarita()
        elif pizzaSecimi == '3':
            secilenPizza = TurkPizza()
        elif pizzaSecimi == '4':
            secilenPizza = SadePizza()
        else:
            print("Yanlış seçim yaptınız.")     
    return secilenPizza

def sosSectir():
    secilenSos = None
    while secilenSos is None:
        sosSecimi = input("Bir sos seciniz: ")
        if sosSecimi == '11':
            secilenSos = Zeytin()
        elif sosSecimi == '12':
            secilenSos = Mantar()
        elif sosSecimi == '13':
            secilenSos = KeciPeyniri()
        elif sosSecimi == '14':
            secilenSos = Et()
        elif sosSecimi == '15':
            secilenSos = Sogan()
        elif sosSecimi == '16':
            secilenSos = Misir()
        else:
            print("Yanlış seçim yaptınız.")    
    return secilenSos

def main():
    with open('menu.txt', 'r') as f:
        print(f.read())

    print("""#######################################
          """)

    pizza = pizzaSectir()
    print(pizza.name, "pizzasini sectiniz.")
    sos = sosSectir()
    print(sos.name, "sosunu sectiniz.")
    tutar = pizza.get_cost() + sos.get_cost()

    print("Secilen Pizza:", pizza.name)
    print("Secilen Sos:", sos.name)
    print("Tutar:", pizza.get_cost() + sos.get_cost())

    isim = input("Isminizi giriniz: ")
    tcNo = input("TC numaranizi giriniz: ")
    krediKartiNo = input("Kredi karti numaranizi giriniz: ")
    krediKartiSifre = input("Kredi karti sifrenizi giriniz: ")
    date = str(datetime.datetime.now())
    siparisAciklama = pizza.description + sos.description
    
    order_df = pd.DataFrame({"pizza":pizza.name, "sos":sos.name, "tutar":tutar, "isim":isim, "tcNo":tcNo, "krediKartiNo":krediKartiNo, "krediKartiSifre":krediKartiSifre, "tarih":date, "aciklama":siparisAciklama}, index=[0])

    order_df.to_csv("Orders_Database.csv")
    
    print("Siparişiniz alinmistir...")
    input("Cikmak için bir tusa basiniz...")

main()