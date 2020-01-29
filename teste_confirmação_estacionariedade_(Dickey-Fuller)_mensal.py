import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

def adf_teste(y):
    #Perfomance do teste ADF
    print('Resultado do teste Dickey-Fuller:')
    df_teste = adfuller(y, autolag = 'AIC')
    df_saida = pd.Series(df_teste[0:4], index = ['Teste', 'Valor p', '# de lags', '# de observações'])
    for k, valor in df_teste[4].items():
        df_saida[f'Valores críticos ({k})'] = valor
    print(df_saida)

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

#Aplicação dp teste ADF nos meses com diferenciação de 1º Ordem
adf_teste(jan_diff)
adf_teste(fev_diff)
adf_teste(mar_diff)
adf_teste(abr_diff)
adf_teste(mai_diff)
adf_teste(jun_diff)
adf_teste(jul_diff)
adf_teste(ago_diff)
adf_teste(set_diff)
adf_teste(out_diff)
adf_teste(nov_diff)
adf_teste(dez_diff)

#Aplicação de diferenciação de 2º Ordem nos meses onde o valor de p > 0.05, após o teste
jun_diff2 = np.diff(jun_diff)
ago_diff2 = np.diff(ago_diff)
out_diff2 = np.diff(out_diff)
dez_diff2 = np.diff(dez_diff)

#Aplicação do teste ADF nos meses que receberam a diferenciação de 2º Ordem
adf_teste(jun_diff2)
adf_teste(ago_diff2)
adf_teste(out_diff2)
adf_teste(dez_diff2)

''' Após aplicar a diferenciação de 1ª ordem, e de 2º ordem em alguns meses,
    a série temporal não-estacionária dos meses virou estacionária após a aplicação
    do teste de Dickey-Fuller confirmou que o valor p < 0.05, rejeitando a hipótese
    nula e confirmando a estacionariedade para a série temporal dos meses.
    OBS: Para o mês de outubro, especificamente, decidi que o valor p séra considerado
    estacionário, mas poderia sim aplicar uma diferenciação de 3º ordem para baixar
    o valor de p.'''