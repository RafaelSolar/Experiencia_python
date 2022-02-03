# Importamos las bibliotecas que se utilizarán, incluyendo nuestro script de funciones
import funciones_ADALINE as fa
import pandas as pd


VecW_final, ldt, MSE_total = [] , [], [] #Creamos listas vacias
for i in range(0,5): #Este for es para poder concatenar las listas y así poder crear un dataframe como el que pide el ejercicio
    r = fa.ajustarW() #Manda a llamar la función para crear un perceptron con las muestras de entrenamiento
    VecW_final.append(r[1]) #Creamos una lista de arrays de los vectores ajustados de los cinco procesos
    #Agremamos listas de datos para el dataframe de los resultados obtenidos en cada entrenamiento
    ldt.append([r[0][0], r[0][1], r[0][2], r[0][3],r[0][4],
                r[1][0], r[1][1], r[1][2], r[1][3],r[1][4],
                r[2]])
    MSE_total.append(r[3]) #Le agregamos a la lista de los MSE
    
col = ["W0i","W1i","W2i","W3i","W4i","W0f","W1f","W2f","W3f","W4f","Épocas"] #Creamos una lista con el nombre de las columnas
ind = ["T1","T2","T3","T4","T5"] #Creamos una lista con el nombre de las filas
tabla1 = pd.DataFrame(data=ldt , columns=col, index= ind) #Creamos un datafrmae
print("\n\n")
print("\t Tabla 'Resultados del entrenamiento del perceptron'")
print()
print(tabla1.head(5))#Imprimimos el dataframe
tabla1.to_csv("Entrenamiento_ADALINE.csv") #Creamos un excel de dicho dataframe

Data3 = [] #Creamos una lista vacia
vecX_eva , vecdata3 = fa.vectorX_evaluacion() #Obtenemos los datos para la evaluacion
#En este for vamos a evaluar cada red, dependiendo la clase
for i in range(0,len(vecX_eva)):
    vxe = []
    vxe = vecdata3[i]
    for j in range(0,5): #En este for validamos las redes
        u = (VecW_final[j]).dot(vecX_eva[i]) #Calculamos u
        #vxe.append(fa.senal(u)) 
        vxe.append("A") if fa.senal(u) == -1 else vxe.append("B") #Clacificamos A o B
    Data3.append(vxe) #Agregamos a la lista
print("\n\n")
col3 = ["X1","X2","X3","X4","Y(T1)","Y(T2)","Y(T3)","Y(T4)","Y(T5)"]#Creamos una lista con el nombre de las columnas
ind3 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]#Creamos una lista con el nombre de las filas
tabla3 = pd.DataFrame(data=Data3 , columns=col3, index= ind3)#Creamos un datafrmae
print("\n\n")
print("\t Tabla 'Validación de redes ADALINE' ")
print()
print(tabla3)
tabla3.to_csv("Evaluacion_ADALINE.csv")#Creamos un excel de dicho dataframe

fa.graph_MSE_mult(MSE_total) #Graficamos la primera y segunda grafica de MSE