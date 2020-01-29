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

#Aplicando a diferenciação de 1º Ordem em todos os bimestres
b1_diff = np.diff(b1)
b2_diff = np.diff(b2)
b3_diff = np.diff(b3)
b4_diff = np.diff(b4)
b5_diff = np.diff(b5)
b6_diff = np.diff(b6)

#Aplicação do teste KPSS nos meses com diferenciação de 1º Ordem
kpss_test(b1_diff)
kpss_test(b2_diff)
kpss_test(b3_diff)
kpss_test(b4_diff)
kpss_test(b5_diff)
kpss_test(b6_diff)

'''Diferente do teste de Dickey-Fuller, o valor p > 0.05 indica que a série é
   estacionária, depois de aplicar a diferenciação de 1º ordem. ''' 