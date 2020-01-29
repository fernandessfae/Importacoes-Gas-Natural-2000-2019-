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

#Aplicando a diferenciação de 1º Ordem em todos os trimestres
t1_diff = np.diff(t1)
t2_diff = np.diff(t2)
t3_diff = np.diff(t3)
t4_diff = np.diff(t4)

#Fazer o teste de estacionaridade da série temporal de todos os trimestres
kpss_test(t1)
kpss_test(t2)
kpss_test(t3)
kpss_test(t4)

'''Diferente do teste de Dickey-Fuller, o valor p > 0.05 indica que a série é
   estacionária, depois de aplicar a diferenciação de 1º ordem. ''' 