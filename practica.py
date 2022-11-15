# consume los datos del archivo de inversiones
# almacena en un dataframe el NOM_EMS, la superficie y el TIPUSSOL
# gráfico de dispersión de los importes de inversiones por TIPUSSOL
# gráfico de barras de la inversión media de los 10 primeros NOM_ENS
# grafico circular de las inversiones de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv('Classificaci%C3%B3_del_s%C3%B2l.csv')
df = datos[['TIPUSSOL','SUPERFICIE','NOM_ENS']]

def dispersion():
    df.plot.scatter(x='NOM_ENS',y='SUPERFICIE',alpha=0.3)
    plt.show()

#dispersion()

def barras():
    valor=df.groupby('NOM_ENS')['SUPERFICIE'].mean()
    valor.head(10).plot.barh()
    plt.show()
#barras()

def circulo():
    df.NOM_ENS.value_counts().plot.pie()
    plt.show()
circulo()