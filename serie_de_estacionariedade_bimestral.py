import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

def teste_adf(y):
    #Teste de performance Augmented Dickey Fuller (ADF)
    print(f'Resultado do Teste Dickey-Fuller para os bimestres : ')
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

#Criação das colunas bimestrais
data['BIMESTRE1'] = data[['JAN', 'FEV']].sum(axis=1)
data['BIMESTRE2'] = data[['MAR', 'ABR']].sum(axis=1)
data['BIMESTRE3'] = data[['MAI', 'JUN']].sum(axis=1)
data['BIMESTRE4'] = data[['JUL', 'AGO']].sum(axis=1)
data['BIMESTRE5'] = data[['SET', 'OUT']].sum(axis=1)
data['BIMESTRE6'] = data[['NOV', 'DEZ']].sum(axis=1)

#Seleção da coluna bimestral
b1 = data.iloc[:, 16]
b2 = data.iloc[:, 17]
b3 = data.iloc[:, 18]
b4 = data.iloc[:, 19]
b5 = data.iloc[:, 20]
b6 = data.iloc[:, 21]

#Fazer o teste de estacionaridade da série temporal de todos os meses
teste_adf(b1)
teste_adf(b2)
teste_adf(b3)
teste_adf(b4)
teste_adf(b5)
teste_adf(b6)

''' Como o valor de P > 0.05, aqui comprova que a série não é estacionária.
    Vale ressaltar que pelo gráfico da série temporal já percebe-se que a série
    não é estacionária, porém é interessante fazer o teste para corroboração.'''