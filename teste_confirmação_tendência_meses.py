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

#Separação da importação de gás natural do meses
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

#Teste de confimação de tendência mensais
mk_test(data_jan)
mk_test(data_fev)
mk_test(data_mar)
mk_test(data_abr)
mk_test(data_mai)
mk_test(data_jun)
mk_test(data_jul)
mk_test(data_ago)
mk_test(data_set)
mk_test(data_out)
mk_test(data_nov)
mk_test(data_dez)
