# Importamos las bibliotecas que se utilizarán.
import numpy as np
import matplotlib.pyplot as plt 
import random as rd
import pandas as pd
import math as mt



def helper_res(epoch, vecWlist, vecW):
    """
    Función para imprimir por pantalla los resultados del entrenamiento
    Entradas: Epoch => Número de epocas realizadas en el entrenamiento
              VecWlist => Vector de pesos inicial 
              vecW => Vector de pesos ajustado
    """
    
    print("Resultados:")
    print("\nÉpocas: {}".format(epoch))
    print("Valores iniciales:\n")
    print("theta = {} \t w1 = {} \t w2 = {} \t w3 = {} \t w4 = {}".format(vecWlist[0],vecWlist[1],vecWlist[2],vecWlist[3], vecWlist[4]))
    print("\nValores finales:\n")
    print("theta = {} \t w1 = {} \t w2 = {} \t w3 = {} \t w4 = {}".format(vecW[0],vecW[1],vecW[2],vecW[3],vecW[4]))

def senal(value):
    """
    Función de activación bipolar step
    Entrada: value => Representa el potencial de activación (u).
    Salida: Retorna 1 si u es mayor o igual a cero y -1 si u es menor a cero
    """
    if value >= 0:
        return 1.
    return -1.

def matriz_x_d():
    """
    Función para crear el conjunto de muestras para el entrenamiento de un perceptron.
    Salidas: vecX => Retornamos un array del conjunto de muestras seleccionadas.
             vecD => Retonamos una lista con las salidas correspondientes a las muestras seleccionadas
    """
    s_t = pd.read_csv("set_entrenamientocsv.csv") #Creamos el dataframe s_t de la tabla valores_ejemplo_1.csv
    colum, filas = s_t.shape
    vecX, vecD = [], [] #Creamos listas vacias
    for j in range(0,colum):
        datapos = s_t.iloc[j]
        xk = [] #Cremos una lista vacia
        for i in datapos[:-1]: #Con este for agregaremos cada elemento de la fila a expeción de la d a la lista X_n
            xk.append(i)
        vecX.append(xk)
        vecD.append(datapos[-1]) #Agregamos las saludas deseadas a una lista
    vecX = np.round(np.array(vecX),4) #Redondemaos los valores con 4 decimas
    return vecX,vecD

def vectorX_evaluacion():
    """
    Recabamos en un array los vectores para la evaluacion,
    así como, para el dataframe.
    """
    #Creamos el dataframe s_t de la tabla valores_ejemplo_1.csv
    s_t = pd.read_csv("set_evaluacioncsv.csv") 
    filas, colum = s_t.shape #Obtenemos el numero de columnas y filas del dataframe
    vecX, vecX_data = [], [] #Creamos listas vacias
    #Con este for obtenemos los datos para evaluar
    for j in range(0,filas):
        datapos = s_t.iloc[j] #Accedemos a la posición j del dataframe
        xk = [] #Cremos una lista vacia
        #Con este for agregaremos cada elemento de la fila a expeción de la d a la lista X_n
        for i in datapos[:]: 
            xk.append(i)
        vecX_data.append(xk[1:]) #Agregamos a la lista desde el segundo elemento al último
        vecX.append(xk)
    vecXarray = np.round(np.array(vecX),4)#Redondemaos los valores con 4 decimas
    return vecXarray, vecX_data


def mean_2_error(vecW):
    """
    Esta función calcula el MSE
    Entrada => vecW es el vector de pesos
    """
    #Obtenemos las muestras de entrenamiento
    vecX , vecD = matriz_x_d()
    #Inicializamos el MSE a cero
    MSE = 0
    #Le asignamos el valor a p (n muestras)
    p = len(vecD)
    for i in range(0,len(vecD)):
        u = vecW.dot(vecX[i]) #Calculamos u
        MSE += mt.pow(vecD[i] - u,2) #Calculamos (d(k) - u)^2 y lo sumamos a MSE 
    MSE /= p #Dividimos el la sumatoria entre p
    return MSE


def graph_MSE(vecMSE):
    """
    Esta función gráfica el error con los
    valores obtenidos en el entrenamiento
    """
    plt.plot(vecMSE)
    plt.xlabel("epochs")
    plt.ylabel("E(w)")
    plt.title("{}".format("MSE vs Épocas"))
    plt.grid()
    plt.show() #Mostramos la gráfica

def graph_MSE_mult(MSE_list):
    """
    Esta función gráfica una superposición 
    de las gráficas 
    """
    plt.xlabel("epochs")
    plt.ylabel("E(w)")
    plt.title("{}".format("MSE vs Épocas"))
    plt.grid()
    colores, grosor = ["r","b"], [2,1] #Caracteriticas de las curvas
    for i  in range(0,2):
        plt.plot(MSE_list[i], c = colores[i], lw = grosor[i])
    plt.show() #Mostramos la gráfica


def ajustarW(vecWi=[] ):
    """
    Función que ajusta el vector de pesos dado, o de lo contrario lo creará con valores aleatorios,
    este ajuste será de acuerdo a las muestras de entrenamiento dadas.
    Utilizando la regla Delta
    Entradas:
              vecWi => vector de pesos inicial.
    Salidas: veclist => Vector de pesos inicial
             vecW => Vector de pesos ajustado
             epoch => Número de épocas realizadas
    """
    if len(vecWi) != 4 : #Si se da un vector erroneo, el programa asigna valores aleatorios
        #Creamos valores aleatorios para los pesos
        weightx0, weightx1 , weightx2 = round(rd.random(),4), round(rd.random(),4), round(rd.random(),4)
        weightx3, weightx4 = round(rd.random(),4), round(rd.random(),4)
        vecWlist = [weightx0, weightx1 , weightx2, weightx3, weightx4] #Creamos una lista para guardar los valores iniciales
        vecW = np.array(vecWlist) #Creamos un array con los valores de la lista de vectones iniciales.
    else:
        vecWlist = vecWi #Creamos la lista de vecotres inicial dada en la entrada
        vecW = np.round(np.array(vecWlist),4) #Creamos un array con los valores de la lista de vectones iniciales.
    n_rt = 0.0025 #Definimos el factor de aprendizaje
    epsilon = mt.pow(10,-6) #Definimos la precisión
    vectors = matriz_x_d() #Mandamos a llamar a la funcion matriz_x_d con las muestras de entramiento dadas.
    vecX , vecD = vectors[0], vectors[1] #Separammos el vector X del vector d
    u, epoch,diff =0,0,1 #Inicializamos en cero las variables necesarias
    MSE_lista = [] #Creamos una lista de error medio para la gráfica
    MSE_lista.append(mean_2_error(vecW))

    while diff > epsilon: #Con este while ejecutamos el algoritmo de entrenamiento
        MSE_previus = mean_2_error(vecW) #Calculamos el MSE_previus
        for i in range(0,len(vecD)):
            u = vecW.dot(vecX[i])
            vecW += (n_rt*(vecD[i] - u))*vecX[i]
        epoch += 1
        MSE_current = mean_2_error(vecW) #Calculamos el MSE_current
        MSE_lista.append(MSE_current) #Agregamos a la lista
        print(MSE_current)
        diff = mt.fabs(MSE_current - MSE_previus) #Calculamos la diferencia de errores.
    vecW = np.round(vecW,4)
    helper_res(epoch, vecWlist, vecW) #Mandamos a llamar a la funcion que imprime los resultados.
    graph_MSE(MSE_lista) #Grafica los resultados.
    return vecWlist , vecW , epoch, MSE_lista

a=ajustarW()
print(a[3])