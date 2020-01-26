import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')
data['BIMESTRE1'] = data[['JAN', 'FEV']].sum(axis=1)
data['BIMESTRE2'] = data[['MAR', 'ABR']].sum(axis=1)
data['BIMESTRE3'] = data[['MAI', 'JUN']].sum(axis=1)
data['BIMESTRE4'] = data[['JUL', 'AGO']].sum(axis=1)
data['BIMESTRE5'] = data[['SET', 'OUT']].sum(axis=1)
data['BIMESTRE6'] = data[['NOV', 'DEZ']].sum(axis=1)

b1 = data.iloc[:, [0, 17]]
b2 = data.iloc[:, [0, 18]]
b3 = data.iloc[:, [0, 19]]
b4 = data.iloc[:, [0, 20]]
b5 = data.iloc[:, [0, 21]]
b6 = data.iloc[:, [0, 22]]

#Histograma de importação de todo o 1º bimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(b1.iloc[:, 0], b1.iloc[:, 1], color = '#0000FF')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 1º bimestre (mil m³)')

#Histograma de importação de todo o 2º bimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(b2.iloc[:, 0], b2.iloc[:, 1], color = '#FF0000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 2º bimestre (mil m³)')

#Histograma de importação de todo o 3º bimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(b3.iloc[:, 0], b3.iloc[:, 1], color = '#FFFF00')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 3º bimestre (mil m³)')

#Histograma de importação de todo o 4º bimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(b4.iloc[:, 0], b4.iloc[:, 1], color = '#008000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 4º bimestre (mil m³)')

#Histograma de importação de todo o 5º bimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(b5.iloc[:, 0], b5.iloc[:, 1], color = '#FF4500')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 5º bimestre (mil m³)')

#Histograma de importação de todo o 6º bimestre de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(b6.iloc[:, 0], b6.iloc[:, 1], color = '#8B008B')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado no 6º bimestre (mil m³)')

#Histograma com todos os bimestres de 2000 a 2019
barWidth = 0.1
plt.figure(figsize = (20, 5))
r1 = np.arange(len(data.iloc[:, 0]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
plt.bar(r1, b1.iloc[:, 1], width = barWidth, color = '#FA8072', label = '1º bimestre')
plt.bar(r2, b2.iloc[:, 1], width = barWidth, color = '#E9967A', label = '2º bimestre')
plt.bar(r3, b3.iloc[:, 1], width = barWidth, color = '#FFA07A', label = '3º bimestre')
plt.bar(r4, b4.iloc[:, 1], width = barWidth, color = '#FF7F50', label = '4º bimestre')
plt.bar(r5, b5.iloc[:, 1], width = barWidth, color = '#FF6347', label = '5º bimestre')
plt.bar(r6, b6.iloc[:, 1], width = barWidth, color = '#FF0000', label = '6º bimestre')