import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import kpss

def kpss_test(y):
    #Teste com o KPSS
    print('Resultado com o teste KPSS')
    kpss_teste = kpss(y)
    kpss_saida = pd.Series(kpss_teste[0:4], index = ['Status KPSS', 'Valor p', '# de lags',
                                                     '# de observações' ])
    for k, valor in kpss_teste[3].items():
        kpss_saida[f'Valores críticos ({k})'] = valor
    print(kpss_saida)

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')

#Anexação do ano no índex da variável para a visualização da série temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')
data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',',
                   parse_dates = ['ANO'], index_col ='ANO', date_parser = dateparse)

anual = data.iloc[:, 15]

#Aplicando a diferenciação de 1º Ordem em todos os anos
anual_diff = np.diff(anual)

#Fazer o teste de estacionaridade da série temporal de todos os anos
kpss_test(anual)

'''Diferente do teste de Dickey-Fuller, o valor p > 0.05 indica que a série é
   estacionária, depois de aplicar a diferenciação de 1º ordem. ''' 