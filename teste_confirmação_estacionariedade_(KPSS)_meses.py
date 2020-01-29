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

#Separando os meses de todos os anos
data_jan = data.iloc[:, 4]
data_fev = data.iloc[:, 5]
data_mar = data.iloc[:, 6]
data_abr = data.iloc[:, 7]
data_mai = data.iloc[:, 8]
data_jun = data.iloc[:, 9]
data_jul = data.iloc[:, 10]
data_ago = data.iloc[:, 11]
data_set = data.iloc[:, 12]
data_out = data.iloc[:, 13]
data_nov = data.iloc[:, 14]
data_dez = data.iloc[:, 15]

#Aplicando a diferenciação de 1º Ordem em todos os meses
jan_diff = np.diff(data_jan)
fev_diff = np.diff(data_fev)
mar_diff = np.diff(data_mar)
abr_diff = np.diff(data_abr)
mai_diff = np.diff(data_mai)
jun_diff = np.diff(data_jun)
jul_diff = np.diff(data_jul)
ago_diff = np.diff(data_ago)
set_diff = np.diff(data_set)
out_diff = np.diff(data_out)
nov_diff = np.diff(data_nov)
dez_diff = np.diff(data_dez)

#Aplicação do teste KPSS nos meses com diferenciação de 1º Ordem
kpss_test(jan_diff)
kpss_test(fev_diff)
kpss_test(mar_diff)
kpss_test(abr_diff)
kpss_test(mai_diff)
kpss_test(jun_diff)
kpss_test(jul_diff)
kpss_test(ago_diff)
kpss_test(set_diff)
kpss_test(out_diff)
kpss_test(nov_diff)
kpss_test(dez_diff)

'''Diferente do teste de Dickey-Fuller, o valor p > 0.05 indica que a série é
   estacionária, depois de aplicar a diferenciação de 1º ordem. '''