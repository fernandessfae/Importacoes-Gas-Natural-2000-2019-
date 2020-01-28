import pandas as pd
from statsmodels.tsa.stattools import adfuller

def teste_adf(y):
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

#Seleção das colunass trimestrais
t1 = data.iloc[:, 16]
t2 = data.iloc[:, 17]
t3 = data.iloc[:, 18]
t4 = data.iloc[:, 19]

#Fazer o teste de estacionaridade da série temporal de todos os trimestres
teste_adf(t1)
teste_adf(t2)
teste_adf(t3)
teste_adf(t4)

''' Como o valor de P > 0.05, aqui comprova que a série não é estacionária.
    Vale ressaltar que pelo gráfico da série temporal já percebe-se que a série
    não é estacionária, porém é interessante fazer o teste para corroboração.'''
