import pandas as pd
from statsmodels.tsa.stattools import adfuller

def teste_adf(y):
    #Teste de performance Augmented Dickey Fuller (ADF)
    print(f'Resultado do Teste Dickey-Fuller para o ano : ')
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

anual = data.iloc[:, 15]

#Fazer o teste de estacionaridade da série temporal de todos os quadrimestres
teste_adf(anual)

''' Como o valor de P > 0.05, aqui comprova que a série não é estacionária.
    Vale ressaltar que pelo gráfico da série temporal já percebe-se que a
    série não é estacionária, porém é interessante fazer o teste para corroboração.'''