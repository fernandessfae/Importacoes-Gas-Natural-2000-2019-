import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',')

ano = data.iloc[:, [0, 16]]

#Histograma de importação de todo o 1º semestre de 2000 a 2019
plt.figure(figsize = (20, 5))
plt.bar(ano.iloc[:, 0], ano.iloc[:, 1], color = 'Orange')
plt.xticks(data['ANO'])
plt.xlabel('Anos')
plt.ylabel('Gás natural importado (mil m³)')
plt.title('Quantidade de gás natural importado por ano (mil m³)')