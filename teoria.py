# https://naps.com.mx/blog/ejemplos-en-matplotlib-de-5-tipos-graficos/

import pandas as pd
import matplotlib.pyplot as plt

def consumirHistograma():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM','CRIM','TOWN','TAX']] # convertir datos en data frame
    #print(df)

    df.RM.plot.hist()
    plt.show()

#consumirHistograma()

def consumirDispersion():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir datos en data frame
    #print(df)

    df.plot.scatter(x='CRIM', y='MEDV', alpha=0.2)
    plt.show()
#consumirDispersion()

def consumirBarras():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir datos en data frame
    #print(df)
    valor_por_ciudad =df.groupby('TOWN') ['MEDV'].mean()
    valor_por_ciudad.head(5).plot.barh()
    plt.show()

#consumirBarras()

def consumirCajas():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir datos en data frame
    #print(df)

    df.head(10).boxplot(column='MEDV', by='TOWN',figsize=(8, 6))
    plt.show()

#consumirCajas()

def consumirCirculo():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df = datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir datos en data frame
    #print(df)

    df.CRIM.head(10).value_counts().plot.pie()
    plt.show()

consumirCirculo()