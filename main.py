import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
wykres.set_ylabel('liczba dzieci')
wykres.set_xlabel('rok')
wykres.legend()
plt.title('Liczba urodzonych dzieci w każdym roku')
plt.show()

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar()
wykres.set_ylabel('liczba dzieci')
wykres.set_xlabel('Płeć')
wykres.legend()
plt.title('Ilość urodzonych dzieci z podziałem na płeć')
plt.show()

ndf = (df[((df.Rok >= 2012) & (df.Rok <= 2017))])

grupa = ndf.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=16, figsize=(5,5), legend=(0,0))
plt.legend(loc="upper right")
plt.title('Ilość urodzonych dzieci z podziałem na płeć')
plt.show()

# zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
 print(df)

 #zadanie 2

 print(df[df['Liczba']<1000])

 print(df.loc[df['Imie'] == 'TOMASZ'])
 print(df['Liczba'].sum())

 new_df = (df[((df.Rok >= 2005) & (df.Rok <= 2010))])
 print(new_df['Liczba'].sum())

 new_df = (df[((df.Rok == 2010) & (df.Plec == 'M'))])
 print(new_df['Liczba'].sum())

for year in range(2000, 2018):
    ndf = (df[((df.Rok == year) & (df.Plec == 'M'))])
    print(ndf.iloc[ndf.Liczba.argmax(), 0:4])

 for year in range(2000, 2018):
     ndf = (df[((df.Rok == year) & (df.Plec == 'K'))])
     print(ndf.iloc[ndf.Liczba.argmax(), 0:2])

 ndf = df.loc[df['Plec'] == 'M']
 grouped = ndf.groupby(['Imie'])

 men = grouped.get_group()
 print(men)