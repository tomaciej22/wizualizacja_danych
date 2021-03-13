#zad1
# zbior_A = [1-x for x in range(1,11)]
# print(zbior_A)
# zbior_B = [4**y for y in range(11)]
# print(zbior_B)
# zbior_C = [z for z in zbior_B if (z%2 == 0)]
# print(zbior_C)
#zad2
# import random
# losowe = []
# for x in range(9):
#     losowe.append(random.randint(1, 30))
# print(losowe)
# parzyste = [x for x in losowe if x % 2 == 0]
# print(parzyste)
#zad3
# produkty = {"bułki": "sztuki", "mąka": "kg", "gruszki": "sztuki", "śliwki": "sztuki"}
# lista = [keys for keys, values in produkty.items() if values == "sztuki"]
# print(produkty)
# print(lista)
#zad4
# def spr_trj(a,b,c):
#     if((a^2+b^2)==c^2):
#         print("OK")
#     else:
#         print("NIE OK")
# spr_trj(3,4,5)
#zad5
# def pol_trapeza(a=1,b=2,h=2):
#     wynik = ((a+b)*h)/2
#     return wynik
# print(pol_trapeza())
#zad6
# def ciag(a=1,b=4,ile=10):
#     for i in range(ile):
#         a*=b
#     return a
# print(ciag())
#zad7
# def ciag2(* cos):
#     a = 1
#     for i in cos:
#         a*=4
#     return a
# print(ciag2(1,2,3,4,5,6,7,8,9,10))
#zad8
# zakupy = {"maka": 1, "cukier": 2, "chleb": 3}
# def lista(a):
#     b = 0
#     c = 0
#     for x in a.values():
#         b += x
#         c += 1
#     print('Wartość:', b, "\nIlosc: ")
#     return c
# print(lista(zakupy))
#zad9
# from ciagi import arytmetyczny, geometryczny
# arytmetyczny.aryt()
# geometryczny.geo()
