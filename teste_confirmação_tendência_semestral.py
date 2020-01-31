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

#Criação das colunas semestrais
data['SEMESTRE1'] = data[['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN']].sum(axis=1)
data['QUADRIMESTRE2'] = data[['JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']].sum(axis=1)

#Seleção das colunas semestrais
s1 = data.iloc[:, 16]
s2 = data.iloc[:, 17]

#Teste de confirmação de tendência semestrais
mk_test(s1)
mk_test(s2)