import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def teste_adf(y):
    #Teste de performance Augmented Dickey Fuller (ADF)
    print(f'Resultado do Teste Dickey-Fuller para os semestres : ')
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
data['SEMESTRE1'] = data[['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN']].sum(axis=1)
data['SEMESTRE2'] = data[['JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']].sum(axis=1)

#Seleção das colunas quadrimestrais
s1 = data.iloc[:, 16]
s2 = data.iloc[:, 17]

#Fazer o teste de estacionaridade da série temporal de todos os quadrimestres
teste_adf(s1)
teste_adf(s2)