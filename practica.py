import pandas as pd

print('Practica')
#muestra un grafico
#de uso de m3 y de número de clientes

def mostrar_grafico():
    datos=pd.read_csv('C:\\Users\\Tecnicos\\Desktop\\DAM\\PROGRAMACIÓN\\servicioagua.csv')
    #print(datos)
    df=datos[['Ús','m3_registrats','num_clients']]
    #print(df)
    # histograma
    df.m3_registrats().plot.hist()
    plt.show()

    # grafico de barras
    m3_por_uso = df.groupby("Ús")["m3_registrars"].mean()
    m3_por_uso.head(10).plot.barh()
    plt.show()

mostrar_grafico()
