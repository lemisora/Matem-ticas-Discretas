import numpy as np

#Se solicitan las dimensiones de la matriz
celdas = int(input("Indica la cantidad de filas y columnas: "))

#Llenamos la matriz de ceros para un uso más fácil
A = np.zeros((celdas,celdas))

print("Matriz de ceros: \n")
print(A)

#Se llena la matriz con unos y ceros según se desee
for i in range(celdas):
    for j in range(celdas):
        print("Indica el valor de A[",i,"][",j,"]: ",end="")
        A[i][j] = int(input(""))
        
print("Nueva matriz: ")
print(A)

# si es reflexiva

R=1

for i in range(celdas):
    if (A[i][i]==0):
        R=0
        

# si es transitiva

T=1

for i in range(celdas):
    for j in range(celdas):
        for k in range(celdas):
            if(A[i][j]==1 and A[j][k]==1 and A[i][k]==0):
                T=0
        

#si es Antisimetrica

a=1

for i in range(celdas):
    for j in range(celdas):
        if(A[i][j]==1 and A[j][i]==0 and i!=j):
            a=0

#si es simetrica

S=1

for i in range(celdas):
    for j in range(celdas):
        if(A[i][j]==1 and A[j][i]==0):
            S=0

#si es de equivalencia, imprimimos las clases      
if(R==1 and S==1 and T==1):
    print("la matriz es de equivalencia ")
    for i in range(celdas):
        print("Clase [",i,"]={ ",end="")
        for j in range(celdas):
            if (A[i][j]==1):
                print(j,"",end="")
        print("}")

# si es de orden
else: 
    if (R==1 and a==1 and T==1):
        print("La matriz es de orden ")