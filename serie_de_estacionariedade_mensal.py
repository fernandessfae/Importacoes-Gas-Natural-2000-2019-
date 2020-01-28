import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def teste_adf(y):
    #Teste de performance Augmented Dickey Fuller (ADF)
    print(f'Resultado do Teste Dickey-Fuller para o meses : ')
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

#Separação da importação de gás natural de todos os meses 
janeiro = data.iloc[:, 3]
fevereiro = data.iloc[:, 4]
março = data.iloc[:, 5]
abril = data.iloc[:, 6]
maio = data.iloc[:, 7]
junho = data.iloc[:, 8]
julho = data.iloc[:, 9]
agosto = data.iloc[:, 10]
setembro = data.iloc[:, 11]
outubro = data.iloc[:, 12]
novembro = data.iloc[:, 13]
dezembro = data.iloc[:, 14]

#Fazer o teste de estacionaridade da série temporal de todos os meses
teste_adf(janeiro)
teste_adf(fevereiro)
teste_adf(março)
teste_adf(abril)
teste_adf(maio)
teste_adf(junho)
teste_adf(julho)
teste_adf(agosto)
teste_adf(setembro)
teste_adf(outubro)
teste_adf(novembro)
teste_adf(dezembro)

''' Como o valor de P > 0.05, aqui comprova que a série não é estacionária.
    Vale ressaltar que pelo gráfico da série temporal já percebe-se que a série
    não é estacionária, porém é interessante fazer o teste para corroboração.'''