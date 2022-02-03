# Importamos las bibliotecas que se utilizarán, incluyendo nuestro script de funciones
import funciones_perc as tw
import random as rd
import pandas as pd
import numpy as np


VecWl, ldt = [] , [] #Creamos listas vacias
for i in range(0,5): #Este for es para poder concatenar las listas y así poder crear un dataframe como el que pide el ejercicio
    r = tw.ajustarW() #Manda a llamar la función para crear un perceptron con las muestras de entrenamiento
    VecWl.append(r[1]) #Creamos una lista de arrays de los vectores ajustados de los cinco procesos
    #Agremamos listas de datos para el dataframe
    ldt.append([r[0][0], r[0][1], r[0][2], r[0][3],
                r[1][0], r[1][1], r[1][2], r[1][3],
                r[2]])
    
col = ["W0i","W1i","W2i","W3i","W0f","W1f","W2f","W3f","Épocas"] #Creamos una lista con el nombre de las columnas
ind = ["T1","T2","T3","T4","T5"] #Creamos una lista con el nombre de las filas
tabla1 = pd.DataFrame(data=ldt , columns=col, index= ind) #Creamos un datafrmae
print("\n\n")
print("\t Tabla 'Resultados del entrenamiento del perceptron'")
print()
print(tabla1.head(5))#Imprimimos el dataframe
tabla1.to_csv("Entrenamiento.csv") #Creamos un excel de dicho dataframe

Data3 = []
for i in range(0,10):
    vxs = tw.x_n(i) #Mandamos a llamar los vectores x para la evalucaión
    vecX = np.array(vxs) #Creamos un array del vector de evaluación
    for j in range(0,5): #En este for validamos el perceptron
        vecWfinal = np.array(VecWl[j]) 
        u = (vecWfinal).dot(vecX)
        vxs.append(tw.senal(u))
    vxs = vxs[1:]
    Data3.append(vxs)

print("\n\n")
col3 = ["X1","X2","X3","Y(T1)","Y(T2)","Y(T3)","Y(T4)","Y(T5)"]#Creamos una lista con el nombre de las columnas
ind3 = ["1","2","3","4","5","6","7","8","9","10"]#Creamos una lista con el nombre de las filas
tabla3 = pd.DataFrame(data=Data3 , columns=col3, index= ind3)#Creamos un datafrmae
print("\n\n")
print("\t Tabla 'Muestras de aceite para validar la red Perceptron' ")
print()
print(tabla3)
tabla3.to_csv("muestras.csv")#Creamos un excel de dicho dataframe

for i in range(0,5): #En este ciclo graficamos los planos finales con las muestras desconocidas
    tw.grafica_3D_PF(VecWl[i])