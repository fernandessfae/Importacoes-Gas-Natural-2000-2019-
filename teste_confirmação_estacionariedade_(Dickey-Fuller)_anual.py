import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

anual = data.iloc[:, 15]

#Fazer o teste de estacionaridade da série temporal de todos os anos
adf_teste(anual)

#Aplicando a diferenciação de 1º Ordem em todos anos
anual_diff = np.diff(anual)

#Aplicação do teste ADF nos anos com diferenciação de 1º Ordem
adf_teste(anual_diff)

#Aplicando a diferenciação de 2º Ordem em todos os anos
anual_diff2 = np.diff(anual_diff)

#Aplicação do teste ADF nos anos com diferenciação de 2º Ordem
adf_teste(anual_diff2)

'''Logo após a aplicação de diferenciação de de 2º ordem, todos os anos
   viraram estacionários com valor p < 0.05.'''

#Visualização do gráfico antes e depois da diferenciação de 2º Ordem   
plt.figure(figsize = (10, 5))
plt.subplot(2, 1, 1)
plt.title('Antes da diferenciação de 2ª Ordem')
plt.plot(anual)

plt.subplot(2, 1, 2)
plt.title('Depois da diferenciação de 2ª Ordem')
plt.plot(anual_diff2)
plt.tight_layout()