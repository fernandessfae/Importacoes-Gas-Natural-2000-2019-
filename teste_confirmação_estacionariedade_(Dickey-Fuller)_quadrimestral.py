import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

def adf_teste(y):
    #Teste de performance Augmented Dickey Fuller (ADF)
    dfteste = adfuller(y, autolag = 'AIC')
    dfsaida = pd.Series(dfteste[0:4], index = ['Teste', 'Valor p', '# de lags', '# de observações'])
    for chave, valor in dfteste[4].items():
        dfsaida[f'Valores críticos ({chave})'] = valor
    print(dfsaida)

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')

#Anexação do ano no índex da variável para a visualização da série temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')
data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',',
                   parse_dates = ['ANO'], index_col ='ANO', date_parser = dateparse)

#Criação das colunas quadrimestrais
data['QUADRIMESTRE1'] = data[['JAN', 'FEV', 'MAR', 'ABR']].sum(axis=1)
data['QUADRIMESTRE2'] = data[['MAI', 'JUN', 'JUL', 'AGO']].sum(axis=1)
data['QUADRIMESTRE3'] = data[['SET', 'OUT', 'NOV', 'DEZ']].sum(axis=1)

#Seleção das colunas quadrimestrais
q1 = data.iloc[:, 16]
q2 = data.iloc[:, 17]
q3 = data.iloc[:, 18]

#Fazer o teste de estacionaridade da série temporal de todos os quadrimestres
adf_teste(q1)
adf_teste(q2)
adf_teste(q3)

#Aplicando a diferenciação de 1º Ordem em todos os quadrimestres
q1_diff = np.diff(q1)
q2_diff = np.diff(q2)
q3_diff = np.diff(q3)

#Aplicação dp teste ADF nos meses com diferenciação de 1º Ordem
adf_teste(q1_diff)
adf_teste(q2_diff)
adf_teste(q3_diff)

'''Logo após a aplicação de diferenciação de de 1º ordem, todos os quadrimestres
   viraram séries estacionárias, com valor p < 0.05.'''