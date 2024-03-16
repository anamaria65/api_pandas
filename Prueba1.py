import requests
import pandas as pd
import matplotlib.pyplot as plt
 
def sacarTemp():
    url= 'https://www.el-tiempo.net/api/json/v2/home'

    response= requests.get(url)
    #Verificar la solicitud
    if response.status_code==200: 
        #Convertimos los datos json a un diccionario
        data= response.json()

        #Creampos una lista para los datos
        ciudades = []
        temperatura_max = []
        temperatura_min = []

        #Lo vamos añadiendo a la lista
        for ciudad in data["ciudades"]:
            ciudades.append(ciudad["name"])
            temperatura_max.append(int(ciudad["temperatures"]["max"]))
            temperatura_min.append(int(ciudad["temperatures"]["min"]))

        #Creamos el DataFrame
        df= pd.DataFrame({
            'Ciudad':ciudades,
            'Temperatura Máx (°C)': temperatura_max,
            'Temperatura Min (°C)':temperatura_min
        })

        #Guardamos el DataFrame en un csv
        df.to_csv('datos_tiempo.csv',index=False, encoding='utf-8')

        print("Los datos se guardaron correctamente")

    else:
        print("Error al obtener los datos de la API")
        
def crearGrafico():
    #Leemps el csv
    df=pd.read_csv('datos_tiempo.csv')
    #Tamaño grafico
    plt.figure(figsize=(10,6))

    #Grafico para las temperaturas
    plt.bar(df['Ciudad'], df['Temperatura Máx (°C)'], color='red', label='Temperatura Máx')
    plt.bar(df['Ciudad'],df['Temperatura Min (°C)'], color='blue', label='Temperatura Mín')

    plt.xlabel('Ciudad')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperaturas Máximas y Mínimas por Ciudad')

    #Rotacion a 45 y lo colocamos a la derecha
    plt.xticks(rotation=45, ha='right')

    #Añade una leyenda para proporcionar informacion sobre los datos
    plt.legend()
    
    # Mostramos el gráfico
    plt.tight_layout() #ajusta automáticamente la disposición de los elementos del gráfico
    plt.show()

sacarTemp()
crearGrafico()

