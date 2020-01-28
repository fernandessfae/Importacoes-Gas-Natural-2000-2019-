import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')

#Anexação do ano no índex da variável para a visualização da série temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')
data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',',
                   parse_dates = ['ANO'], index_col ='ANO', date_parser = dateparse)

anual = data.iloc[:, 15]

#Visualização do gráfico da série tanual
plt.figure(figsize = (10, 5))
plt.xlabel('Anos')
plt.ylabel('Quantidade de gás natural importado no 2º semestre (mil m³)')
plt.plot(anual)

#Decomposição da série temporal anual
decomposicao = seasonal_decompose(anual)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
residuo = decomposicao.resid

#Visualização da tendência, sazionalidade e resíduo da série temporal
plt.plot(tendencia)
plt.plot(sazonal)
plt.plot(residuo)

plt.figure(figsize = (10, 5))
plt.subplot(4, 1, 1)
plt.plot(anual, label = 'Ano')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(residuo, label = 'Residuo')
plt.legend(loc = 'best')
plt.tight_layout()