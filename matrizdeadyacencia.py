import numpy as np                  #libreria para trabajar con matrices
import matplotlib.pyplot as plt     #libreria para trabajar con grafos         
import networkx as nx               #programa principal


#funciones

def matriz_adyacencia(n):
    #n es el numero de vertices
    #matriz de adyacencia
    matriz = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            print("Ingrese el valor de la matriz en la posicion [",i,",",j,"]")
            matriz[i,j] = int(input())
    return matriz


def visualizar_matriz(matriz):
    #visualizar la matriz de adyacencia
    plt.imshow(matriz)                  #visualizar la matriz   aqui si no quieres que se vea mamon nomas ponle un print(matriz)
    plt.show()                          #mostrar la matriz
    
def conexo(matriz):
    #verificar si el grafo es conexo
    #si la matriz es simetrica es conexo
    #si la matriz es asimetrica es no conexo
    if np.array_equal(matriz,matriz.T):
        print("El grafo es conexo")
    else:
        print("El grafo es no conexo")
        
def grafo_entrada(matriz):
    #grafo de entrada
    #para cada vertice, el grafo de entrada es el conjunto de vertices que tienen aristas dirigidas hacia el vertice
    #matriz de adyacencia de entrada
    matriz_entrada = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if matriz[i,j] == 1:
                matriz_entrada[i,j] = 1
    return matriz_entrada

def grafo_salida(matriz):
    #grafo de salida
    #para cada vertice, el grafo de salida es el conjunto de vertices que tienen aristas dirigidas desde el vertice
    #matriz de adyacencia de salida
    matriz_salida = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if matriz[i,j] == 1:
                matriz_salida[j,i] = 1
    return matriz_salida

def grafo_total(matriz):
    #grafo total
    #para cada vertice, el grafo total es el conjunto de vertices que tienen aristas dirigidas hacia o desde el vertice
    #matriz de adyacencia de total
    matriz_total = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if matriz[i,j] == 1:
                matriz_total[i,j] = 1
                matriz_total[j,i] = 1
    return matriz_total

def caminos_2(matriz):
    #caminos de longitud 2
    #para cada vertice, el conjunto de caminos de longitud 2 es el conjunto de caminos de longitud 2 que tienen como extremos el vertice
    #matriz de adyacencia de caminos de longitud 2
    matriz_caminos_2 = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if matriz[i,j] == 1:
                for k in range(n):
                    if matriz[j,k] == 1:
                        matriz_caminos_2[i,k] = 1
    return matriz_caminos_2

def caminos_3(matriz):
    #caminos de longitud 3
    #para cada vertice, el conjunto de caminos de longitud 3 es el conjunto de caminos de longitud 3 que tienen como extremos el vertice
    #matriz de adyacencia de caminos de longitud 3
    matriz_caminos_3 = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if matriz[i,j] == 1:
                for k in range(n):
                    if matriz[j,k] == 1:
                        for l in range(n):
                            if matriz[k,l] == 1:
                                matriz_caminos_3[i,l] = 1
    return matriz_caminos_3

def visualizar_grafo(matriz):
    #visualizar el grafo
    G = nx.from_numpy_matrix(matriz)
    nx.draw(G,with_labels=False)
    plt.show()
    
#programa principal

n = int(input("Ingrese el número de vértices del grafo: "))
matriz = matriz_adyacencia(n)
visualizar_matriz(matriz)
conexo(matriz)
#menu de opciones
print("1. Grafo de entrada")
print("2. Grafo de salida")    
print("3. Grafo total")
print("4. Caminos de longitud 2")  
print("5. Caminos de longitud 3")
print("6. Salir")

opcion = int(input("Ingrese la opcion que desee: "))
while opcion != 6:
    if opcion == 1:
        matriz_entrada = grafo_entrada(matriz)
        visualizar_grafo(matriz_entrada)
    elif opcion == 2:
        matriz_salida = grafo_salida(matriz)
        visualizar_grafo(matriz_salida)
    elif opcion == 3:
        matriz_total = grafo_total(matriz)
        visualizar_grafo(matriz_total)
    elif opcion == 4:
        matriz_caminos_2 = caminos_2(matriz)
        visualizar_grafo(matriz_caminos_2)
    elif opcion == 5:
        matriz_caminos_3 = caminos_3(matriz)
        visualizar_grafo(matriz_caminos_3)
    else:
        print("Opción inexistente")
    opcion = int(input("Ingrese la opcion que desee: "))
    
    










