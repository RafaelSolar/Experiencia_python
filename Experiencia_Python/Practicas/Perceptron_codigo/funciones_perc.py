# Importamos las bibliotecas que se utilizarán.
import numpy as np
import matplotlib.pyplot as plt 
import random as rd
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D



def helper_res(epoch, vecWlist, vecW, ajuste_done):
    """
    Función para imprimir por pantalla los resultados del entrenamiento
    Entradas: Epoch => Número de epocas realizadas en el entrenamiento
              VecWlist => Vector de pesos inicial 
              vecW => Vector de pesos ajustado
              ajuste_done => Número de ajustes hechos
    """
    
    print("Resultados:")
    print("\nÉpocas: {}".format(epoch))
    print("Valores iniciales:\n")
    print("theta = {} \t w1 = {} \t w2 = {} \t w3 = {}".format(vecWlist[0],vecWlist[1],vecWlist[2],vecWlist[3]))
    print("\nValores finales:\n")
    print("theta = {} \t w1 = {} \t w2 = {} \t w3 = {}".format(vecW[0],vecW[1],vecW[2],vecW[3]))
    print("Ajustes hechos: {}".format(ajuste_done))

def senal(value):
    """
    Función de activación bipolar step
    Entrada: value => Representa el potencial de activación (u).
    Salida: Retorna 1 si u es mayor o igual a cero y -1 si u es menor a cero
    """
    if value >= 0:
        return 1.
    return -1.

def ajuste(vweight, vx, y, d, n):
    """
    Función que ajusta el vector de pesos vectorialmente
    Entradas: vweight => Es el vector de pesos anterior
              vx => Es el vector de muestra x(k)
              y => Es la salida del perceptron
              d => Es la salida deseada
              n => Es el factor de aprendizaje
    Salida: Retorna la operación de ajuste para el vector de pesos.
    """
    return vweight + (n*(d-y))*vx

def x_n(pos):
    
    """
    Esta función nos retorna los vectores para la validación (x1,x2,x3)
    Entradas: pos => Es la posición que queremos de nuestro archivo cvs empezando desde 0.
    Salidas: X_n => vector X
    """
    s_t = pd.read_csv("valores_tabla3.csv") #Creamos el dataframe s_t de la tabla valores_tabla3.csv
    datapos = s_t.iloc[pos] #Del dataframe seleccionamos la fila en la posición pos
    X_n = [] #Creamos una lista vacia
    for e in datapos[:]: #Con este for agregaremos cada elemento de la fila a la lista X_n
        X_n.append(e)
    return X_n


def matriz_x_d():
    """
    Función para crear el conjunto de muestras para el entrenamiento de un perceptron.
    Salidas: vecX => Retornamos un array del conjunto de muestras seleccionadas.
             vecD => Retonamos una lista con las salidas correspondientes a las muestras seleccionadas
    """
    s_t = pd.read_csv("valores_ejemplo_1.csv") #Creamos el dataframe s_t de la tabla valores_ejemplo_1.csv
    vecX, vecD = [], [] #Creamos listas vacias
    for j in range(0,30):
        datapos = s_t.iloc[j]
        xk = [] #Cremos una lista vacia
        for i in datapos[:-1]: #Con este for agregaremos cada elemento de la fila a expeción de la d a la lista X_n
            xk.append(i)
        vecX.append(xk)
        vecD.append(datapos[-1]) #Agregamos las saludas deseadas a una lista
    vecX = np.array(vecX)
    return vecX,vecD

def z_3D(vecW, x ,y ):
    """
    Función para crear la función del plano 3D
    Entradas: vecW => Vector de pesos
              x => Valores de la coordenada x
              y => Valores de la coordenada y
    """
    mx1 = vecW[1]/vecW[3] #Creamos la variable mx1
    mx2 = vecW[2]/vecW[3] #Creamos la variable mx2
    b = vecW[0]/vecW[3] #Creamos la variable b
    return -mx1*x - mx2*y + b 

def grafica_3D(X_D,vecW,flag = 1): 
    """
    Función para crear la gráfica en 3D
    Entradas X_D => Es la lista que contiene el array con las muestras para el entrenamiento.
             vecW => Es el vector de pesos
             flag => Si es 1 graficará junto con el plano, si es 0 solo graficará los puntos.
    """
    Xmtx = np.asmatrix(X_D[0]) #Creamos una matriz con las muestras de entrenamiento
    xtra = np.transpose(Xmtx) #transponemos la matriz para poder operar eficiente.
    points = [] #Creamos una lista vacia
    for i in range(1,4): #Mediante este for creamos una lista que contiene tres listas de los puntos x1,x2,x3
        li_p = xtra[i].tolist()[0]
        points.append(li_p)
    # Creamos el plano 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = points[0], points[1],points[2] #Creamos los variables para el conjunto de puntos x,y,z de las muestras
    for i in range(0,30): #Mediante este for asiganará un color de punto (x,y,z) diferente dependiendo de la salida esperada
        if X_D[1][i] == 1:
            ax.scatter(x[i], y[i], z[i], c='g', marker='.')
        else:
            ax.scatter(x[i], y[i], z[i], c ='r', marker='.')
    ax.scatter(0, 0,0, c ='b', marker='o') #Creamos el centro de la gráfica 3D
    if flag == 1:
        x = np.linspace(-1.5,3,30) #Delimitamos el rango en x
        y = np.linspace(-1.5,3,30) #Delimitamos el rango en y
        X, Y = np.meshgrid(x,y) #Devuelve una lista de matrices de coordenadas a partir de vectores de coordenadas
        ax.plot_surface(X,Y,z_3D(vecW,X,Y)) #Creamos el plano frontera
        plt.show() #Mostramos la gráfica con puntos y plano
    else:
        plt.show()#Mostramos  la gráfica solo con los puntos.

def grafica_3D_PF(vecW):
    """
    Esta función gráfica el plano del vector de pesos proporcioando junto con los puntos finales para análisis
    Entradas: vecW => Vector de pesos
    """
    # Creamos el plano 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    s_t = pd.read_csv("valores_tabla3.csv") #Creamos el dataframe de la tabla de valores_tabla3
    for i in range(0,10): #Con este for colocamos todos los puntos para analizar
        xyz=list(s_t.iloc[i][1:])
        ax.scatter(xyz[0], xyz[1], xyz[2], c='g', marker='.')
    x = np.linspace(-1.5,3,30) #Delimitamos el rango en x
    y = np.linspace(-1.5,3,30) #Delimitamos el rango en y  
    X, Y = np.meshgrid(x,y) #Devuelve una lista de matrices de coordenadas a partir de vectores de coordenadas.
    ax.plot_surface(X,Y,z_3D(vecW,X,Y)) #Creamos el plano frontera
    plt.show() #Mostramos la gráfica
    
    
def ajustarW(vecWi=[]):
    """
    Función que ajusta el vector de pesos dado, o de lo contrario lo creará con valores aleatorios, este ajuste será de acuerdo
    a las muestras de entrenamiento dadas.
    Utilizando la regla de Hebb
    Entradas:
              vecWi => vector de pesos inicial.
    Salidas: veclist => Vector de pesos inicial
             vecW => Vector de pesos ajustado
             epoch => Número de épocas realizadas
    """
    if len(vecWi) != 4 : #Si se da un vector erroneo, el programa asigna valores aleatorios
        #Creamos valores aleatorios para los pesos
        weightx0, weightx1 , weightx2, weightx3 = round(rd.random(),4), round(rd.random(),4), round(rd.random(),4), round(rd.random(),4)
        vecWlist = [weightx0, weightx1 , weightx2, weightx3] #Creamos una lista para guardar los valores iniciales
        vecW = np.array(vecWlist) #Creamos un array con los valores de la lista de vectones iniciales.
    else:
        vecWlist = vecWi #Creamos la lista de vecotres inicial dada en la entrada
        vecW = np.round(np.array(vecWlist),4) #Creamos un array con los valores de la lista de vectones iniciales.
    ratelearning = 0.01 #Definimos el factor de aprendizaje
    vectors = matriz_x_d() #Mandamos a llamar a la funcion matriz_x_d con las muestras de entramiento dadas.
    vecX , vecD = vectors[0], vectors[1] #Separammos el vector X del vector d
    u, epoch, compro, ajuste_done =0,0,0,0 #Inicializamos en cero las variables necesarias

    while compro <30: #Durante este ciclo comprobamos que las 30 salidas deseadas correspondiente del perceptron
                      #sean igual a la salida del perceptron.
        compro = 0 #Inicializamos a cero la variable compro para que en cada ciclo el conteo de comrprobaciones empiece en cero
        #print("Época {}:".format(epoch+1)) #Imprimimos por pantalla en la epoca que se encuentra el algoritmo
        for i in range(0,30):
            u = (vecW).dot(np.transpose(vecX[i])) #Calcula potencial de activación
            y = senal(u) #Determina la salida del perceptron
            if y != vecD[i]:
                vecW = np.round(ajuste(vecW, vecX[i], y, vecD[i],ratelearning),4) #Ajusta el vector de pesos
                ajuste_done +=1 #Le suma uno a la variable de ajustes hechos
            else:
                compro +=1 #Le suma una unidad a la variable compro
        #print("\n")
        epoch +=1 #Le suma una unidad a la variable epoch

    helper_res(epoch, vecWlist, vecW,ajuste_done) #Mandamos a llamar a la funcion que imprime los resultados.
    grafica_3D(vectors, vecW) #Grafica los resultados.
    return vecWlist , vecW , epoch