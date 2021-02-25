# zad1
a = 'napis'
b = 'napis2'
print(a, b)
# zad2
a = 2
b = 2
print(a + b)
print(a - b)
print(a / b)
print(a ** b)
print(a * b)
# zad3
c, d, e, f, g, h = 2, 2, 2, 2, 2, 2
c += 2
d -= 2
h *= 2
g /= 2
f **= 2
e %= 2
print(c,d,h,g,f,e)
#zad5
imie = 'TOMASZ'
nazwisko = 'KARKULOWSKI'
zmiennaimie = imie.capitalize()
zmiennanazwisko = nazwisko.capitalize()
print(zmiennaimie, zmiennanazwisko)
#zad6
tekst = ['siaba', 'siaba']
x = tekst.count("siaba")
print(x)
#zad7
imie = 'stefan'
print(imie[1], imie[5])
#zad8
tekst = 'siaba siaba siaba'
y = tekst.split(" ")
print(y)
#zad9
a = str("cos")
b = float(1.8)
c = hex(2)
print('cos %(zm)s i %(zm2)f i %(zm3)g ' % {'zm': a, 'zm2': b, 'zm3': c})