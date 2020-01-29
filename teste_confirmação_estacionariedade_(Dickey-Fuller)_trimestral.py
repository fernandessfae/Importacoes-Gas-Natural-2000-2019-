import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

def adf_teste(y):
    #Teste de performance Augmented Dickey Fuller (ADF)
    print(f'Resultado do Teste Dickey-Fuller para os trimestres : ')
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

#Criação das colunas trimestrais
data['TRIMESTRE1'] = data[['JAN', 'FEV', 'MAR']].sum(axis=1)
data['TRIMESTRE2'] = data[['ABR', 'MAI', 'JUN']].sum(axis=1)
data['TRIMESTRE3'] = data[['JUL', 'AGO', 'SET']].sum(axis=1)
data['TRIMESTRE4'] = data[['OUT', 'NOV', 'DEZ']].sum(axis=1)

#Seleção das colunas trimestrais
t1 = data.iloc[:, 16]
t2 = data.iloc[:, 17]
t3 = data.iloc[:, 18]
t4 = data.iloc[:, 19]

#Fazer o teste de estacionaridade da série temporal de todos os trimestres
adf_teste(t1)
adf_teste(t2)
adf_teste(t3)
adf_teste(t4)

#Aplicando a diferenciação de 1º Ordem em todos os bimestres
t1_diff = np.diff(t1)
t2_diff = np.diff(t2)
t3_diff = np.diff(t3)
t4_diff = np.diff(t4)

#Aplicação dp teste ADF nos meses com diferenciação de 1º Ordem
adf_teste(t1_diff)
adf_teste(t2_diff)
adf_teste(t3_diff)
adf_teste(t4_diff)

'''Logo após a aplicação de diferenciação de de 1º ordem, todos os trimestres
   viraram séries estacionárias, com valor p < 0.05. '''