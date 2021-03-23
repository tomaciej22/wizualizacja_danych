import sys
import random
#zad1
# plik = open("D:\do pythona\zad1.txt", "w+", encoding='utf-8')
# lista = []
# for x in range(31):
#     x*2
#     x = lista.append(random.randint(0, 30))
# plik = open("D:\do pythona\zad1.txt", "w+", encoding='utf-8')
# plik.writelines(str(lista))
# plik.close()
#zad2
# with open("D:\do pythona\zad1.txt", "r") as plik:
#     for linia in plik:
#         print(linia)
#zad3
# with open("D:\do pythona\zad2.txt", "w+") as plik:
#     dane = input("Napisz cos: ")
#     plik.write(dane)
#     plik.close()
# with open("D:\do pythona\zad2.txt", "r") as plik:
#     for linia in plik:
#         print(linia)
#zad4
# class NaZakupy():
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
#     def ile_produktu(self):
#         help = 0
#         if type(self.jednostka_miary) is type(help):
#             print(self.ilosc+self.jednostka_miary)
#         else:
#             print(self.ilosc, self.jednostka_miary)
#     def ile_kosztuje(self):
#         return self.cena_jed*self.ilosc
# lista_zakupow = NaZakupy("Mąka", 5, "kg", 10)
# lista_zakupow.wyswietl_produkt()
# lista_zakupow.ile_produktu()
# print(lista_zakupow.ile_kosztuje())
#zad5
class Ciag():
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
    def wyswietl_dane(self):
        print("Wyswietl dane:")
        print("a1: ", self.a1)
        print("r: ", self.r)
        print("n: ", self.n)
    def pobierz_elementy(self):
        print("Pobierz elementy:")
        print("a1:", self.a1)
        print("r:", self.r)
        print("n:", self.n)
    def pobierz_parametry(self):
        print("Pobierz parametry:")
        print("a1:", self.a1)
        print("r:", self.r)
        print("n:", self.n)
    def policz_sume(self):
        self.a1 = int(a1)
        self.r = int(r)
        self.n = int(n)
        print("Policz sume:")
        print(((2*self.a1+(self.n-1)*self.r)/2)*self.n)
    def policz_elementy(self):
        print("Policz elementy:")
        self.a1 = int(a1)
        self.r = int(r)
        self.n = int(n)
        lista = []
        if (self.a1 and self.r and self.n == 0):
            print("Podaj wartosci")
        else:
            for x in range(0,self.n):
                self.a1+=self.r
                lista.append(self.a1)
            print(lista)
a1 = input("Podaj a1: ")
r = input("Podaj r: ")
n = input("Podaj n: ")
wyswietl = Ciag(a1, r ,n)
wyswietl.wyswietl_dane()
wyswietl.pobierz_elementy()
wyswietl.pobierz_parametry()
wyswietl.policz_sume()
wyswietl.policz_elementy()

