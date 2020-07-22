import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

#Anexação do ano no índex da variável para a visualização da série temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')
data = pd.read_csv('importacao-gas-natural-2000-2019-m3.csv', delimiter = ';', decimal = ',',
                   parse_dates = ['ANO'], index_col ='ANO', date_parser = dateparse)

#Transformação da produção de mil m³ para m³ somente
def mul_colunas(lista_features):
    for i in lista_features:
        data[i] = data[i].truediv(1000)
mul_colunas(['JAN','FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ', 'TOTAL'])

#Separação dos bimestres
data['BIMESTRE1'] = data[['JAN', 'FEV']].sum(axis = 1)
data['BIMESTRE2'] = data[['MAR', 'ABR']].sum(axis = 1)
data['BIMESTRE3'] = data[['MAI', 'JUN']].sum(axis = 1)
data['BIMESTRE4'] = data[['JUL', 'AGO']].sum(axis = 1)
data['BIMESTRE5'] = data[['SET', 'OUT']].sum(axis = 1)
data['BIMESTRE6'] = data[['NOV', 'DEZ']].sum(axis = 1)

b1 = data.iloc[:, 16]
b2 = data.iloc[:, 17]
b3 = data.iloc[:, 18]
b4 = data.iloc[:, 19]
b5 = data.iloc[:, 20]
b6 = data.iloc[:, 21]

#Visualização do gráfico e da decomposição da série temporal de cada bimestre
def decomposicao(series):
    plt.figure(figsize = (10, 5))
    plt.xlabel('Anos')
    plt.ylabel('Quantidade (m³)')
    if series is b1:
        plt.title('Quantidade de gás natural importado no 1° bimestre', fontsize = 16, fontweight = 'bold')
    elif series is b2:
        plt.title('Quantidade de gás natural importado no 2° bimestre', fontsize = 16, fontweight = 'bold')
    elif series is b3:
        plt.title('Quantidade de gás natural importado no 3° bimestre', fontsize = 16, fontweight = 'bold')
    elif series is b4:
        plt.title('Quantidade de gás natural importado no 4° bimestre', fontsize = 16, fontweight = 'bold')
    elif series is b5:
        plt.title('Quantidade de gás natural importado no 5° bimestre', fontsize = 16, fontweight = 'bold')
    elif series is b6:
        plt.title('Quantidade de gás natural importado no 6° bimestre', fontsize = 16, fontweight = 'bold')
    plt.plot(series)
    
    decomposicao = seasonal_decompose(series)
    tendencia = decomposicao.trend
    sazonal = decomposicao.seasonal
    residuo = decomposicao.resid
    
    plt.figure(figsize = (10, 5))
    plt.subplot(4, 1, 1)
    if series is b1:
        plt.plot(series, label = '1° bimestre')
    elif series is b2:
        plt.plot(series, label = '2° bimestre')
    elif series is b3:
        plt.plot(series, label = '3° bimestre')
    elif series is b4:
        plt.plot(series, label = '4° bimestre')
    elif series is b5:
        plt.plot(series, label = '5° bimestre')
    elif series is b6:
        plt.plot(series, label = '6° bimestre')
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
    
decomposicao(b1)
decomposicao(b2)
decomposicao(b3)
decomposicao(b4)
decomposicao(b5)
decomposicao(b6)
