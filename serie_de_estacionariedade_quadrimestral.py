import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def teste_adf(y):
    #Teste de performance Augmented Dickey Fuller (ADF)
    print(f'Resultado do Teste Dickey-Fuller para os quadrimestres : ')
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
teste_adf(q1)
teste_adf(q2)
teste_adf(q3)

''' Como o valor de P > 0.05, aqui comprova que a série não é estacionária,
    exceto o segundo quadrimestre. Vale ressaltar que pelo gráfico da série
    temporal já percebe-se que a série não é estacionária, porém é interessante
    fazer o teste para corroboração.'''
