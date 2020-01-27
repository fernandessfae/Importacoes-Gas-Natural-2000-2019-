import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')
data['QUADRIMESTRE1'] = data[['JAN', 'FEV', 'MAR', 'ABR']].sum(axis=1)
data['QUADRIMESTRE2'] = data[['MAI', 'JUN', 'JUL', 'AGO']].sum(axis=1)
data['QUADRIMESTRE3'] = data[['SET', 'OUT', 'NOV', 'DEZ']].sum(axis=1)

q1 = data.iloc[:, [0, 17]]
q2 = data.iloc[:, [0, 18]]
q3 = data.iloc[:, [0, 19]]

#Histograma de importação de todo o 1º quadrimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(q1.iloc[:, 0], q1.iloc[:, 1], color = '#0000FF')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 1º quadrimestre (mil m³)')

#Histograma de importação de todo o 2º quadrimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(q2.iloc[:, 0], q2.iloc[:, 1], color = '#FF0000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 2º quadrimestre (mil m³)')

#Histograma de importação de todo o 3º quadrimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(q3.iloc[:, 0], q3.iloc[:, 1], color = '#FFFF00')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 3º quadrimestre (mil m³)')

#Histograma com todos os quadrimestres de 2000 a 2019
barWidth = 0.2
plt.figure(figsize = (20, 5))
r1 = np.arange(len(data.iloc[:, 0]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
plt.bar(r1, q1.iloc[:, 1], width = barWidth, color = '#FFD700', label = '1º quadrimestre')
plt.bar(r2, q2.iloc[:, 1], width = barWidth, color = '#FFFF00', label = '2º quadrimestre')
plt.bar(r3, q3.iloc[:, 1], width = barWidth, color = '#F0E68C', label = '3º quadrimestre')
plt.xticks([r + barWidth for r in range(len(q1.iloc[:, 1]))], data['ANO'], rotation = 'vertical')
plt.xlabel('Anos')
plt.ylabel('Importação gás natural (mil m³)')
plt.title('Quantidade de gás natural importado (2000 - 2019)')
plt.legend(loc = 'best')
plt.show() 
