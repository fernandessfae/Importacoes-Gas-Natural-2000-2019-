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

#Aplicação dp teste ADF nos meses com diferenciação de 1º Ordem
adf_teste(b1_diff)
adf_teste(b2_diff)
adf_teste(b3_diff)
adf_teste(b4_diff)
adf_teste(b5_diff)
adf_teste(b6_diff)

''' Exceto o 3º bimestre, todos os demais bimestres tiveram o valor de p < 0.05
    no teste ADF, fazendo com que se tornassem séries estacionárias.
    OBS: no caso do 3 bimetre, irei considerar a série estacionária, em virtude
    de ser um valor p um pouco maior do que o esperado.'''