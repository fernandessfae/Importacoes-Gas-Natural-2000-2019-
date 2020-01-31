import pandas as pd
from statsmodels.tsa.api import Holt

#Anexação do ano no índex da variável para a visualização da série temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')
data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',',
                   parse_dates = ['ANO'], index_col ='ANO', date_parser = dateparse)

#Criação da coluna bimestral
data['BIMESTRE2'] = data[['MAR', 'ABR']].sum(axis=1)

#Seleção da coluna bimestral
b2 = data.iloc[:, 16]

#Treinamento do modelo Holt Winters simples
fit1 = Holt(b2).fit(smoothing_level = 0.8, smoothing_slope = 0.2, optimized = False)
fcast1 = fit1.forecast(2).rename("Previsão")

#Visualização do gráfico com a previsão simples 
fit1.fittedvalues.plot(marker = 'o', color = 'red')
fcast1.plot(marker = 'o', color = 'black', legend = True)

#Treinamento do modelo Holt Winters amortecida
fit2 = Holt(b2, damped = True).fit(smoothing_level = 0.8, smoothing_slope = 0.2, optimized = True)
fcast2 = fit2.forecast(2).rename("Previsão")

#Visualização do gráfico com a previsão suavizada
fit2.fittedvalues.plot(marker = 'o', color = 'blue')
fcast2.plot(marker = 'o', color = 'orange', legend = True)