import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')
data_jan = data.iloc[:, [0, 4]]
data_fev = data.iloc[:, [0, 5]]
data_mar = data.iloc[:, [0, 6]]
data_abr = data.iloc[:, [0, 7]]
data_mai = data.iloc[:, [0, 8]]
data_jun = data.iloc[:, [0, 9]]
data_jul = data.iloc[:, [0, 10]]
data_ago = data.iloc[:, [0, 11]]
data_set = data.iloc[:, [0, 12]]
data_out = data.iloc[:, [0, 13]]
data_nov = data.iloc[:, [0, 14]]
data_dez = data.iloc[:, [0, 15]]

#Histograma de importação de todos os meses de janeiros de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_jan.iloc[:, 0], data_jan.iloc[:, 1], color = '#0000FF')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em janeiro (mil m³)')

#Histograma de importação de todos os meses de fevereiro de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_fev.iloc[:, 0], data_fev.iloc[:, 1], color = '#FF0000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em fevereiro (mil m³)')

#Histograma de importação de todos os meses de março de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_mar.iloc[:, 0], data_mar.iloc[:, 1], color = '#FFFF00')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em março (mil m³)')

#Histograma de importação de todos os meses de abril de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_abr.iloc[:, 0], data_abr.iloc[:, 1], color = '#008000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em abril (mil m³)')

#Histograma de importação de todos os meses de maio de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_mai.iloc[:, 0], data_mai.iloc[:, 1], color = '#FF4500')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em maio (mil m³)')

#Histograma de importação de todos os meses de junho de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_jun.iloc[:, 0], data_jun.iloc[:, 1], color = '#8B008B')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em junho (mil m³)')

#Histograma de importação de todos os meses de julho de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_jul.iloc[:, 0], data_jul.iloc[:, 1], color = '#FF69B4')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em julho (mil m³)')

#Histograma de importação de todos os meses de agosto de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_ago.iloc[:, 0], data_ago.iloc[:, 1], color = '#8B4513')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em agosto (mil m³)')

#Histograma de importação de todos os meses de setembro de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_set.iloc[:, 0], data_set.iloc[:, 1], color = '#000000')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em setembro (mil m³)')

#Histograma de importação de todos os meses de outubro de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_out.iloc[:, 0], data_out.iloc[:, 1], color = '#00FFFF')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em outubro (mil m³)')

#Histograma de importação de todos os meses de novembro de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_nov.iloc[:, 0], data_nov.iloc[:, 1], color = '#E6E6FA')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em novembro (mil m³)')

#Histograma de importação de todos os meses de dezembro de 2000 a 2019
plt.figure(figsize = (10, 5))
plt.bar(data_dez.iloc[:, 0], data_dez.iloc[:, 1], color = '#F5F5F5')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado em dezembro (mil m³)')

#Histograma com todos os meses de janeiro a dezembro de 2000 a 2019
barWidth = 0.05
plt.figure(figsize = (20, 5))
r1 = np.arange(len(data.iloc[:, 0]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]
r9 = [x + barWidth for x in r8]
r10 = [x + barWidth for x in r9]
r11 = [x + barWidth for x in r10]
r12 = [x + barWidth for x in r11]
plt.bar(r1, data_jan.iloc[:, 1], width = barWidth, color = '#0000FF', label = 'JAN')
plt.bar(r2, data_fev.iloc[:, 1], width = barWidth, color = '#6495ED', label = 'FEV')
plt.bar(r3, data_mar.iloc[:, 1], width = barWidth, color = '#4169E1', label = 'MAR')
plt.bar(r4, data_abr.iloc[:, 1], width = barWidth, color = '#1E90FF', label = 'ABR')
plt.bar(r5, data_mai.iloc[:, 1], width = barWidth, color = '#00BFFF', label = 'MAI')
plt.bar(r6, data_jun.iloc[:, 1], width = barWidth, color = '#87CEFA', label = 'JUN')
plt.bar(r7, data_jul.iloc[:, 1], width = barWidth, color = '#87CEEB', label = 'JUL')
plt.bar(r8, data_ago.iloc[:, 1], width = barWidth, color = '#ADD8E6', label = 'AGO')
plt.bar(r9, data_set.iloc[:, 1], width = barWidth, color = '#4682B4', label = 'SET')
plt.bar(r10, data_out.iloc[:, 1], width = barWidth, color = '#B0C4DE', label = 'OUT')
plt.bar(r11, data_nov.iloc[:, 1], width = barWidth, color = '#836FFF', label = 'NOV')
plt.bar(r12, data_dez.iloc[:, 1], width = barWidth, color = '#6959CD', label = 'DEZ')
plt.xticks([r + barWidth for r in range(len(data_jan.iloc[:, 1]))], data['ANO'], rotation = 'vertical')
plt.xlabel('Anos')
plt.ylabel('Importação gás natural (mil m³)')
plt.title('Quantidade de gás natural importado (2000 - 2019)')
plt.legend(loc = 'best')
plt.show() 
