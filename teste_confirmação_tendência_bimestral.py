import pandas as pd
import pymannkendall

def mk_test(y):
    #teste de mann-kendall
    print('Resultado do Teste Mann-Kendall')
    mkteste = pymannkendall.hamed_rao_modification_test(y)
    mksaida = pd.Series(mkteste[0:9], index = ['Movimento Tendência', 'Há Tendência?', 'Valor p', 'Teste normalizado',
                                               'Coeficiente Kendall', 'Mand-Kendall Score', 'Variância S', 'Sen Slope'])
    print(mksaida)

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

#Teste de confirmação de tendência bimestrais
mk_test(b1)
mk_test(b2)
mk_test(b3)
mk_test(b4)
mk_test(b5)
mk_test(b6)