## Aplicación del modelo K-means usando la biblioteca SKlearn de Python. ##
## Author: Mtro. Christian Mauricio Castillo Estrada <UNACH> 2022
## Analizar comportamiento de las personas tomando en consideración su edad y número de compras por internet

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df = pd.read_csv ('C:/UNACH/DatosPersonasCompras.csv')

# Mostramos las primeras observaciones
print(df.head())
df.plot.scatter(x='Edad', y='ComprasAnual', c='DarkGreen')
plt.show()

min_max_scaler = MinMaxScaler() 
df = min_max_scaler.fit_transform(df)
df = pd.DataFrame(df) # Convertimos a Dataframe

X= df.iloc[:, [1,2]].values 
Inertia=[]
for i in range(1,11):
    kmeans = KMeans(n_clusters= i, init='k-means++', random_state=0)
    kmeans.fit(X)
    Inertia.append(kmeans.inertia_)
    
#Visualización del Metodo del codo
plt.figure(1 , figsize = (9 ,4))
plt.plot(range(1,11), Inertia,'-')
plt.title('Metodo del Codo')
plt.xlabel('N clusters')
plt.ylabel('Inertia')
plt.show() 

##Segmentación de clientes
kmeansmodel = KMeans(n_clusters= 3, init='k-means++', random_state=0)
y_kmeans= kmeansmodel.fit_predict(X)

plt.figure(1 , figsize = (13 ,6))
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'royalblue',   marker="o", label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'green',  marker= "v",label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'maroon',    marker= "^",label = 'Cluster 3')
plt.scatter(kmeansmodel.cluster_centers_[:, 0], kmeansmodel.cluster_centers_[:, 1], s = 100, c = 'orange', label = 'Centroides')
plt.title('Segmentación de Clientes')
plt.xlabel('Edad')
plt.ylabel('Compras Anual por internet')
plt.legend()
plt.show()
