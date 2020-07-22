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

#Separação dos trimestres
data['TRIMESTRE1'] = data[['JAN', 'FEV', 'MAR']].sum(axis = 1)
data['TRIMESTRE2'] = data[['ABR', 'MAI', 'JUN']].sum(axis = 1)
data['TRIMESTRE3'] = data[['JUL', 'AGO', 'SET']].sum(axis = 1)
data['TRIMESTRE4'] = data[['OUT', 'NOV', 'DEZ']].sum(axis = 1)

t1 = data.iloc[:, 16]
t2 = data.iloc[:, 17]
t3 = data.iloc[:, 18]
t4 = data.iloc[:, 19]

#Visualização do gráfico e da decomposição da série temporal de cada trimestre
def decomposicao(series):
    plt.figure(figsize = (10, 5))
    plt.xlabel('Anos')
    plt.ylabel('Quantidade (m³)')
    if series is t1:
        plt.title('Quantidade de gás natural importado no 1° trimestre', fontsize = 16, fontweight = 'bold')
    elif series is t2:
        plt.title('Quantidade de gás natural importado no 2° trimestre', fontsize = 16, fontweight = 'bold')
    elif series is t3:
        plt.title('Quantidade de gás natural importado no 3° trimestre', fontsize = 16, fontweight = 'bold')
    elif series is t4:
        plt.title('Quantidade de gás natural importado no 4° trimestre', fontsize = 16, fontweight = 'bold')
    plt.plot(series)
    
    decomposicao = seasonal_decompose(series)
    tendencia = decomposicao.trend
    sazonal = decomposicao.seasonal
    residuo = decomposicao.resid
    
    plt.figure(figsize = (10, 5))
    plt.subplot(4, 1, 1)
    if series is t1:
        plt.plot(series, label = '1° trimestre')
    elif series is t2:
        plt.plot(series, label = '2° trimestre')
    elif series is t3:
        plt.plot(series, label = '3° trimestre')
    elif series is t4:
        plt.plot(series, label = '4° trimestre')
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
    
decomposicao(t1)
decomposicao(t2)
decomposicao(t3)
decomposicao(t4)