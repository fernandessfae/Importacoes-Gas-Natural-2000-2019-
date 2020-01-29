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

#Criação das colunas semestrais
data['SEMESTRE1'] = data[['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN']].sum(axis=1)
data['QUADRIMESTRE2'] = data[['JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']].sum(axis=1)

#Seleção das colunas semestrais
s1 = data.iloc[:, 16]
s2 = data.iloc[:, 17]

#Fazer o teste de estacionaridade da série temporal de todos os semestres
adf_teste(s1)
adf_teste(s2)

#Aplicando a diferenciação de 1º Ordem em todos os semestres
s1_diff = np.diff(s1)
s2_diff = np.diff(s2)

#Aplicação dp teste ADF nos meses com diferenciação de 1º Ordem
adf_teste(s1_diff)
adf_teste(s2_diff)

'''Logo após a aplicação de diferenciação de de 1º ordem, todos os semestres
   viraram séries estacionárias, com valor p < 0.05.'''