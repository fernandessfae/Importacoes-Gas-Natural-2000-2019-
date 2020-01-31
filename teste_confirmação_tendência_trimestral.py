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

#Teste de confirmação de tendência trimestrais
mk_test(t1)
mk_test(t2)
mk_test(t3)
mk_test(t4)