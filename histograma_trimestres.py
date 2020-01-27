import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')
data['TRIMESTRE1'] = data[['JAN', 'FEV', 'MAR']].sum(axis=1)
data['TRIMESTRE2'] = data[['ABR', 'MAI', 'JUN']].sum(axis=1)
data['TRIMESTRE3'] = data[['JUL', 'AGO', 'SET']].sum(axis=1)
data['TRIMESTRE4'] = data[['OUT', 'NOV', 'DEZ']].sum(axis=1)

t1 = data.iloc[:, [0, 17]]
t2 = data.iloc[:, [0, 18]]
t3 = data.iloc[:, [0, 19]]
t4 = data.iloc[:, [0, 20]]

#Histograma de importação de todo o 1º trimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(t1.iloc[:, 0], t1.iloc[:, 1], color = '#0000FF')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 1º trimestre (mil m³)')

#Histograma de importação de todo o 2º trimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(t2.iloc[:, 0], t2.iloc[:, 1], color = '#FF0000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 2º trimestre (mil m³)')

#Histograma de importação de todo o 3º trimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(t3.iloc[:, 0], t3.iloc[:, 1], color = '#FFFF00')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 3º trimestre (mil m³)')

#Histograma de importação de todo o 4º trimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(t4.iloc[:, 0], t4.iloc[:, 1], color = '#008000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 4º trimestre (mil m³)')

#Histograma com todos os trimestres de 2000 a 2019
barWidth = 0.15
plt.figure(figsize = (20, 5))
r1 = np.arange(len(data.iloc[:, 0]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
plt.bar(r1, t1.iloc[:, 1], width = barWidth, color = '#8A2BE2', label = '1º trimestre')
plt.bar(r2, t2.iloc[:, 1], width = barWidth, color = '#4B0082', label = '2º trimestre')
plt.bar(r3, t3.iloc[:, 1], width = barWidth, color = '#9400D3', label = '3º trimestre')
plt.bar(r4, t4.iloc[:, 1], width = barWidth, color = '#9932CC', label = '4º trimestre')
plt.xticks([r + barWidth for r in range(len(t1.iloc[:, 1]))], data['ANO'], rotation = 'vertical')
plt.xlabel('Anos')
plt.ylabel('Importação gás natural (mil m³)')
plt.title('Quantidade de gás natural importado (2000 - 2019)')
plt.legend(loc = 'best')
plt.show() 